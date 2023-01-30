# edalize_sandpiper_example
Example for using sandpiper with edalize front-end

## Command to run with edalize
```python3 runner.py```

## Command to run with Fusesoc

- Before using fusesoc for the first time add this as a core to the fusesoc library

```fusesoc library add adder .```

- Run the below command to generate the verilog with fusesoc

```fusesoc run --target=sandpiper adder```