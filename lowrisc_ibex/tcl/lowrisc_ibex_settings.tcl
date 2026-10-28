# Include dirs and defines for lowrisc_ibex, appended to the project settings.
set root [file normalize [file dirname [info script]]/../..]
set fs [get_filesets sources_1]
set_property include_dirs [concat [get_property include_dirs $fs] [list \
    $root/vendor/lowrisc_ip/ip/prim/rtl \
    $root/vendor/lowrisc_ip/dv/sv/dv_utils \
]] $fs
set_property verilog_define [concat [get_property verilog_define $fs] [list \
    FPGA_XILINX=1 \
    PRIM_DEFAULT_IMPL=prim_pkg::ImplXilinx \
]] $fs
