from __future__ import annotations

from pathlib import Path
from typing import Any

from tsfpga.hdl_file import HdlFile
from tsfpga.module import BaseModule

PACKAGE = Path(__file__).parent.resolve()
ROOT = PACKAGE.parent

# Synthesis closure of ibex_top as selected by FuseSoC, packages first.
FILES = [
    "vendor/lowrisc_ip/ip/prim/rtl/prim_util_pkg.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi_pkg.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_count_pkg.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_pkg.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_cipher_pkg.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_ram_1p_pkg.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_ram_2p_pkg.sv",
    "lowrisc_ibex/generated/prim_pkg.sv",
    "rtl/ibex_pkg.sv",
    "lowrisc_ibex/generated/prim_and2.sv",
    "lowrisc_ibex/generated/prim_buf.sv",
    "lowrisc_ibex/generated/prim_clock_gating.sv",
    "lowrisc_ibex/generated/prim_clock_inv.sv",
    "lowrisc_ibex/generated/prim_clock_mux2.sv",
    "lowrisc_ibex/generated/prim_flop.sv",
    "lowrisc_ibex/generated/prim_ram_1p.sv",
    "lowrisc_ibex/generated/prim_ram_2p.sv",
    "dv/uvm/icache/dv/prim_badbit/prim_badbit_ram_1p.sv",
    "rtl/ibex_alu.sv",
    "rtl/ibex_branch_predict.sv",
    "rtl/ibex_compressed_decoder.sv",
    "rtl/ibex_controller.sv",
    "rtl/ibex_core.sv",
    "rtl/ibex_counter.sv",
    "rtl/ibex_cs_registers.sv",
    "rtl/ibex_csr.sv",
    "rtl/ibex_decoder.sv",
    "rtl/ibex_dummy_instr.sv",
    "rtl/ibex_ex_block.sv",
    "rtl/ibex_fetch_fifo.sv",
    "rtl/ibex_icache.sv",
    "rtl/ibex_id_stage.sv",
    "rtl/ibex_if_stage.sv",
    "rtl/ibex_load_store_unit.sv",
    "rtl/ibex_lockstep.sv",
    "rtl/ibex_multdiv_fast.sv",
    "rtl/ibex_multdiv_slow.sv",
    "rtl/ibex_pmp.sv",
    "rtl/ibex_prefetch_buffer.sv",
    "rtl/ibex_register_file_ff.sv",
    "rtl/ibex_register_file_fpga.sv",
    "rtl/ibex_register_file_latch.sv",
    "rtl/ibex_top.sv",
    "rtl/ibex_wb_stage.sv",
    "shared/rtl/bus.sv",
    "shared/rtl/ram_1p.sv",
    "shared/rtl/ram_2p.sv",
    "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_and2.sv",
    "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_buf.sv",
    "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_clock_gating.sv",
    "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_clock_inv.sv",
    "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_clock_mux2.sv",
    "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_flop.sv",
    "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_ram_1p.sv",
    "vendor/lowrisc_ip/ip/prim_generic/rtl/prim_generic_ram_2p.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_cdc_rand_delay.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_count.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_fifo_async_simple.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_fifo_async_sram_adapter.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_fifo_async.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_fifo_sync_cnt.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_fifo_sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_flop_2sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_lfsr.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi12_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi12_sender.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi12_sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi16_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi16_sender.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi16_sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi20_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi20_sender.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi20_sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi24_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi24_sender.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi24_sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi28_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi28_sender.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi28_sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi32_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi32_sender.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi32_sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi4_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi4_sender.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi4_sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi8_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi8_sender.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_mubi8_sync.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_onehot_check.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_onehot_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_onehot_mux.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_present.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_prince.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_ram_1p_adv.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_ram_1p_scr.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_22_16_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_22_16_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_28_22_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_28_22_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_39_32_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_39_32_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_64_57_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_64_57_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_72_64_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_72_64_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_22_16_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_22_16_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_39_32_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_39_32_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_72_64_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_72_64_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_76_68_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_hamming_76_68_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_22_16_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_22_16_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_28_22_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_28_22_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_39_32_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_39_32_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_64_57_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_64_57_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_72_64_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_72_64_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_hamming_22_16_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_hamming_22_16_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_hamming_39_32_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_hamming_39_32_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_hamming_72_64_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_hamming_72_64_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_hamming_76_68_dec.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_secded_inv_hamming_76_68_enc.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_subst_perm.sv",
    "vendor/lowrisc_ip/ip/prim/rtl/prim_sync_reqack.sv",
    "vendor/lowrisc_ip/ip/prim_xilinx/rtl/prim_xilinx_and2.sv",
    "vendor/lowrisc_ip/ip/prim_xilinx/rtl/prim_xilinx_buf.sv",
    "vendor/lowrisc_ip/ip/prim_xilinx/rtl/prim_xilinx_clock_gating.sv",
    "vendor/lowrisc_ip/ip/prim_xilinx/rtl/prim_xilinx_clock_mux2.sv",
    "vendor/lowrisc_ip/ip/prim_xilinx/rtl/prim_xilinx_flop.sv",
]

INCLUDE_DIRS = [
    ROOT / "vendor/lowrisc_ip/ip/prim/rtl",
    ROOT / "vendor/lowrisc_ip/dv/sv/dv_utils",
]

DEFINES = {
    "FPGA_XILINX": "1",
    "PRIM_DEFAULT_IMPL": "prim_pkg::ImplXilinx",
}

TCL_SETTINGS = PACKAGE / "tcl" / "lowrisc_ibex_settings.tcl"


class Module(BaseModule):
    def __init__(
        self,
        path: Path,  # noqa: ARG002
        library_name: str,  # noqa: ARG002
        **kwargs: Any,  # noqa: ARG002
    ) -> None:
        super().__init__(path=PACKAGE, library_name="lowrisc_ibex")

    def get_synthesis_files(
        self,
        files_include: set[Path] | None = None,
        files_avoid: set[Path] | None = None,
        **kwargs: Any,  # noqa: ARG002
    ) -> list[HdlFile]:
        paths = [ROOT / f for f in FILES]
        return [
            HdlFile(p)
            for p in paths
            if (files_include is None or p in files_include)
            and (files_avoid is None or p not in files_avoid)
        ]

    def get_simulation_files(
        self,
        files_include: set[Path] | None = None,
        files_avoid: set[Path] | None = None,
        **kwargs: Any,  # noqa: ARG002
    ) -> list[HdlFile]:
        return self.get_synthesis_files(
            files_include=files_include, files_avoid=files_avoid
        )
