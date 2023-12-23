# About Cyecca

[Cyecca](https://github.com/cognipilot/cyecca) is a control and estimation library.  The library leverages [Casadi](http://casadi.org/) based equation graphs and can be thought of the control and estimation equivalent of TensorFlow. The equation graph is used for [automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation), a numerically efficient method for computing jacobians. Casadi's core is written in C, with Python and Matlab wrappers. Cyecca leverages the Python library in Casadi. Casadi allows the user to create advanced geometric algorithms without advanced knowledge of embedded programming. This provides a route for rapid development.

## [B3RB](../../reference_systems/b3rb/about.md) Example

For a complete example of how Cyecca may be used, the [B3RB](https://github.com/CogniPilot/cerebri/tree/25497bf9960c6ca74e98c1709d34c756ac4395a9/app/b3rb/src/casadi/) will be used as an example.

### Generation of Equations

The proceeding leverages the Cyecca library to generate a simple rover estimator in 2D.

```python title="Derive Rover Estimator:"
def derive_rover2d_estimator():
    # define symbols
    x = ca.SX.sym("x")  # x position in world frame of rear axle (north)
    y = ca.SX.sym("y")  # y position in world frame of rear axle (east)
    theta = ca.SX.sym("theta")  # angular heading in world frame (rotation about down)
    u = ca.SX.sym("u")  # forward velocity, along body x
    omega = ca.SX.sym("omega")  # angular velocity around z axis
    dt = ca.SX.sym("dt")  # time stemp

    G = lie.SE2
    X = G.elem(ca.vertcat(x, y, theta))
    v = G.algebra.elem(ca.vertcat(u, 0, omega))

    X1 = X + v
    f_predict = ca.Function(
        "predict", [X.param, omega, u], [X1.param], ["x0", "omega", "u"], ["x1"]
    )

    eqs = {"predict": f_predict}
    return eqs
```

Here the relevant variables of interest are defined.
```python title="Relevant variables of interest:"
    # define symbols
    x = ca.SX.sym("x")  # x position in world frame of rear axle (north)
    y = ca.SX.sym("y")  # y position in world frame of rear axle (east)
    theta = ca.SX.sym("theta")  # angular heading in world frame (rotation about down)
    u = ca.SX.sym("u")  # forward velocity, along body x
    omega = ca.SX.sym("omega")  # angular velocity around z axis
    dt = ca.SX.sym("dt")  # time stemp
```


```python title="SE2 Lie Algebra element:"
    G = lie.SE2  # the SE2 Lie group which describes planar 2D motion
    X = G.elem(ca.vertcat(x, y, theta)) @ 
    v = G.algebra.elem(ca.vertcat(u, 0, omega))
```

The SE2 Lie Algebra element, which describes the rotational and linear movement of the rover
u represents the distance travelled along the arc created with an angular change of omega
these may be thought of at linear and angular velocity multiplied by time.


```python
    X1 = X + v
```

This represents the exact integration in SE(2), there are no numerical integration errors
due to the geometric nature of the integration in the Lie Algebra, one may think of this as 
the Lie Group equivalent of: $x_1 = x_0 + u*dt$, where $x_0$ is the initial state, $x_1$ is the final state, $u$ is the velocity, and $dt$ is the change in time.


```python
    f_predict = ca.Function(
        "predict", [X.param, omega, u], [X1.param], ["x0", "omega", "u"], ["x1"]
    )

    eqs = {"predict": f_predict}
    return eqs
```

Finally the casadi function routine is used to construct and return the prediction function.


#### Code Generation Routines

``` { .py .annotate .no-copy title="Generate code:"}
def generate_code(eqs: dict, filename, dest_dir: str, **kwargs):
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(exist_ok=True)
    p = {
        "verbose": True,
        "mex": False,           #(1)
        "cpp": False,           #(2)
        "main": False,          #(3)
        "with_header": True,    #(4)
        "with_mem": False,      #(5)
        "with_export": False,   #(6)
        "with_import": False,
        "include_math": True,   #(7)
        "avoid_stack": True,    #(8)
    }
    for k, v in kwargs.items():
        assert k in p.keys()
        p[k] = v

    gen = ca.CodeGenerator(filename, p)
    for name, eq in eqs.items():
        gen.add(eq)
    gen.generate(str(dest_dir) + os.se
```

1. Without mex which is used for Matlab.
2. Without cpp since [Cerebri is focused on MISRA C](../../cerebri/about.md#layers-of-verificaiton-and-validation).
3. Without a main function, just use functions in a library.
4. With a header for use in the library.
5. Without mem, as internal memory is not necessary for these routines.
6. Without export, as there is no need for dll export.
7. With math, as this leverages the math routines.
8. With avoid_stack, so the data used for calculations is explicitly passed in and not allocated with the stack of the function.

#### Generating Code

```python
if __name__ == "__main__":
    #rover_plan()
    #plt.show()
    #test_bezier()

    print("generating casadi equations")
    # derivate casadi functions
    eqs = {}
    eqs.update(derive_bezier6())
    eqs.update(derive_rover())
    eqs.update(derive_se2())
    eqs.update(derive_rover2d_estimator())

    for name, eq in eqs.items():
        print('eq: ', name)

    generate_code(eqs, filename="b3rb.c", dest_dir="gen")
    print("complete")
```

This routine generates from each of the relevant equation and creates the b3rb.c file.

It is recommended to use poetry to run Cyecca, a working Poetry [environment](https://github.com/CogniPilot/cyecca/blob/3c23e2830f630872b464c6af3172872c8e1bb075/pyproject.toml) is provided with Cyecca. It is recommended to use this environment to generate the code.

```sh
poetry run -C ~/cognipilot/tools/src/cyecca python3 b3rb.py
```

### Adding Casadi Generated Code to Apps

Next add the generated source files to [CMake](https://github.com/CogniPilot/cerebri/blob/25497bf9960c6ca74e98c1709d34c756ac4395a9/app/b3rb/CMakeLists.txt).

```cmake
if (CONFIG_CEREBRI_B3RB_CASADI)
  list(APPEND SOURCE_FILES
    src/casadi/gen/b3rb.c)
endif()
```

### Calling Casadi based function from Cerebri

It is now straight forward to call the generated Casadi function from within Cerebri.

The [estimator app](https://github.com/CogniPilot/cerebri/blob/25497bf9960c6ca74e98c1709d34c756ac4395a9/app/b3rb/src/estimate.c) collects the necessary information by ***subscribing*** to the following topics:

  * `imu` topic provides the required angular velocity data.
  * `wheel_odometry` topic provides the required distance travelled.

The [estimator app](https://github.com/CogniPilot/cerebri/blob/25497bf9960c6ca74e98c1709d34c756ac4395a9/app/b3rb/src/estimate.c) ***publishes***:

  * `estimator_odometry` topic contains the location the robot believes it is at.


``` { .c .annotate .no-copy title="The Casadi function call:"}
/* predict:(x0[3],omega,u)->(x1[3]) */
{
    double delta_theta = omega * dt;    //(1)
    double x1[3];

    // LOG_DBG("predict");
    CASADI_FUNC_ARGS(predict);
    args[0] = ctx->x;                   //(2)
    args[1] = &delta_theta;             //(3)
    args[2] = &u;                       //(4)
    res[0] = x1;                        //(5)
    CASADI_FUNC_CALL(predict);          //(6)

    // update x, W
    handle_update(ctx, x1);
}
```

1. Given the angular velocity $\omega$ from the z axis of the gyroscope, multiply the delta time $dt$ since the last estimator run, and then compute the angular change $d\theta$ in radians. 
2. Load the function argument for initial state $x_0$ into the Casadi function.
3. Load the function argument for angular velocity $\omega$ into the Casadi function.
4. Load the function argument for velocity $u$ into the Casadi function.
5. Set the result $x_1$ in the res double array.
6. The macro CASADI_FUNC_ARGS allocates the args, res, w (work), iw (integer work) vectors which are used in the function call.

Here the signature is provided in the [generated code](https://github.com/CogniPilot/cerebri/blob/25497bf9960c6ca74e98c1709d34c756ac4395a9/app/b3rb/src/casadi/gen/b3rb.c#L1940)


The macros are defined [here](https://github.com/CogniPilot/cerebri/blob/25497bf9960c6ca74e98c1709d34c756ac4395a9/include/cerebri/core/casadi.h).

```c
#define CASADI\_FUNC\_ARGS(name)              \
    casadi_int iw[name##_SZ_IW];            \
    casadi_real w[name##_SZ_W];             \
    const casadi_real* args[name##_SZ_ARG]; \
    casadi_real* res[name##_SZ_RES];        \
    int mem = 0;

#define CASADI\_FUNC\_CALL(name) \
    name(args, res, iw, w, mem);
```

An Ipython notebook of this example can be found [here](https://github.com/CogniPilot/cyecca/blob/3c23e2830f630872b464c6af3172872c8e1bb075/notebook/Rover2DOdom.ipynb)
