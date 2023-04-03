# edalize_sandpiper_example
Example for using sandpiper with edalize front-end, fusesoc and fusesoc-flow

## Command to run with edalize
```python3 runner.py```

## Command to run with Fusesoc 

### Convert TLV to SV using Sandpiper - Tool Target

- Before using fusesoc for the first time add this as a core to the fusesoc library

```fusesoc library add adder .```

- Run the below command to generate the verilog with fusesoc

```fusesoc run --target=sandpiper adder```

### Convert TLV to SV using Sandpiper and SV to Netlist using Design Compiler - Flow Target
```fusesoc run --target=sp_dc adder --build_root="build_synth"```
