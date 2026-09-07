from __future__ import annotations

import json
import subprocess
from datetime import UTC, datetime
from typing import Any

from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
    CVERaw,
    ImageScanResultRaw,
    ImageVulnerabilityScanPort,
)

_TRIVY_COMMAND_TIMEOUT_SECONDS = 60.0
_KNOWN_SEVERITIES = frozenset({"critical", "high", "medium", "low"})


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut: MutantDict = {}  # type: ignore


class TrivyCVEScanAdapter(ImageVulnerabilityScanPort):
    """Secondary adapter — shells out to the `trivy` CLI. Any scan failure
    (missing binary, timeout, non-zero exit, unparsable output) is returned
    as `scan_status="unscanned"` data, never raised — the scanner being
    unavailable or the image being unreachable (e.g. a private registry) is
    an expected, gracefully-handled state for this feature."""

    @_mutmut_mutated(mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut)
    def scan_image(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_orig(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_1(self, image: str) -> ImageScanResultRaw:
        try:
            result = None
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_2(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                None,
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_3(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=None,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_4(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=None,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_5(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=None,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_6(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_7(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_8(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_9(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_10(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["XXtrivyXX", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_11(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["TRIVY", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_12(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "XXimageXX", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_13(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "IMAGE", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_14(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "XX--formatXX", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_15(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--FORMAT", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_16(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "XXjsonXX", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_17(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "JSON", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_18(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "XX--quietXX", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_19(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--QUIET", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_20(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=False,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_21(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=False,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_22(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode == 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_23(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 1:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_24(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = None
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_25(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(None)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)

    def xǁTrivyCVEScanAdapterǁscan_image__mutmut_26(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(None)

mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['_mutmut_orig'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_1'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_2'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_3'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_4'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_5'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_6'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_7'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_8'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_9'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_10'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_11'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_12'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_13'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_14'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_15'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_16'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_17'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_18'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_19'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_20'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_21'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_22'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_23'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_24'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_25'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTrivyCVEScanAdapterǁscan_image__mutmut['xǁTrivyCVEScanAdapterǁscan_image__mutmut_26'] = TrivyCVEScanAdapter.xǁTrivyCVEScanAdapterǁscan_image__mutmut_26 # type: ignore # mutmut generated
mutants_x__unscanned_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__unscanned_result__mutmut)
def _unscanned_result() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status="unscanned", cves=[], detected_base_image=None, scanned_at=None
    )


def x__unscanned_result__mutmut_orig() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status="unscanned", cves=[], detected_base_image=None, scanned_at=None
    )


def x__unscanned_result__mutmut_1() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status=None, cves=[], detected_base_image=None, scanned_at=None
    )


def x__unscanned_result__mutmut_2() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status="unscanned", cves=None, detected_base_image=None, scanned_at=None
    )


def x__unscanned_result__mutmut_3() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        cves=[], detected_base_image=None, scanned_at=None
    )


def x__unscanned_result__mutmut_4() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status="unscanned", detected_base_image=None, scanned_at=None
    )


def x__unscanned_result__mutmut_5() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status="unscanned", cves=[], scanned_at=None
    )


def x__unscanned_result__mutmut_6() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status="unscanned", cves=[], detected_base_image=None, )


def x__unscanned_result__mutmut_7() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status="XXunscannedXX", cves=[], detected_base_image=None, scanned_at=None
    )


def x__unscanned_result__mutmut_8() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status="UNSCANNED", cves=[], detected_base_image=None, scanned_at=None
    )

mutants_x__unscanned_result__mutmut['_mutmut_orig'] = x__unscanned_result__mutmut_orig # type: ignore # mutmut generated
mutants_x__unscanned_result__mutmut['x__unscanned_result__mutmut_1'] = x__unscanned_result__mutmut_1 # type: ignore # mutmut generated
mutants_x__unscanned_result__mutmut['x__unscanned_result__mutmut_2'] = x__unscanned_result__mutmut_2 # type: ignore # mutmut generated
mutants_x__unscanned_result__mutmut['x__unscanned_result__mutmut_3'] = x__unscanned_result__mutmut_3 # type: ignore # mutmut generated
mutants_x__unscanned_result__mutmut['x__unscanned_result__mutmut_4'] = x__unscanned_result__mutmut_4 # type: ignore # mutmut generated
mutants_x__unscanned_result__mutmut['x__unscanned_result__mutmut_5'] = x__unscanned_result__mutmut_5 # type: ignore # mutmut generated
mutants_x__unscanned_result__mutmut['x__unscanned_result__mutmut_6'] = x__unscanned_result__mutmut_6 # type: ignore # mutmut generated
mutants_x__unscanned_result__mutmut['x__unscanned_result__mutmut_7'] = x__unscanned_result__mutmut_7 # type: ignore # mutmut generated
mutants_x__unscanned_result__mutmut['x__unscanned_result__mutmut_8'] = x__unscanned_result__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_trivy_payload__mutmut)
def _parse_trivy_payload(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_orig(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_1(payload: Any) -> ImageScanResultRaw:
    if isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_2(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = None
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_3(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") and []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_4(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get(None) or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_5(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("XXResultsXX") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_6(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_7(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("RESULTS") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_8(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") and []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_9(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get(None) or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_10(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("XXVulnerabilitiesXX") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_11(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_12(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("VULNERABILITIES") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_13(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = None
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_14(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(None)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_15(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_16(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(None)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_17(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status=None,
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_18(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=None,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_19(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=None,
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_20(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=None,
    )


def x__parse_trivy_payload__mutmut_21(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_22(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_23(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_24(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        )


def x__parse_trivy_payload__mutmut_25(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="XXscannedXX",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_26(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="SCANNED",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_27(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(None),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def x__parse_trivy_payload__mutmut_28(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(None).isoformat(),
    )

mutants_x__parse_trivy_payload__mutmut['_mutmut_orig'] = x__parse_trivy_payload__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_1'] = x__parse_trivy_payload__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_2'] = x__parse_trivy_payload__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_3'] = x__parse_trivy_payload__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_4'] = x__parse_trivy_payload__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_5'] = x__parse_trivy_payload__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_6'] = x__parse_trivy_payload__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_7'] = x__parse_trivy_payload__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_8'] = x__parse_trivy_payload__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_9'] = x__parse_trivy_payload__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_10'] = x__parse_trivy_payload__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_11'] = x__parse_trivy_payload__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_12'] = x__parse_trivy_payload__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_13'] = x__parse_trivy_payload__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_14'] = x__parse_trivy_payload__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_15'] = x__parse_trivy_payload__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_16'] = x__parse_trivy_payload__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_17'] = x__parse_trivy_payload__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_18'] = x__parse_trivy_payload__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_19'] = x__parse_trivy_payload__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_20'] = x__parse_trivy_payload__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_21'] = x__parse_trivy_payload__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_22'] = x__parse_trivy_payload__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_23'] = x__parse_trivy_payload__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_24'] = x__parse_trivy_payload__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_25'] = x__parse_trivy_payload__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_26'] = x__parse_trivy_payload__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_27'] = x__parse_trivy_payload__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_trivy_payload__mutmut['x__parse_trivy_payload__mutmut_28'] = x__parse_trivy_payload__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_cve_raw__mutmut)
def _to_cve_raw(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_orig(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_1(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = None
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_2(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get(None)
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_3(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("XXVulnerabilityIDXX")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_4(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("vulnerabilityid")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_5(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VULNERABILITYID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_6(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = None
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_7(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get(None)
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_8(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("XXSeverityXX")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_9(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_10(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("SEVERITY")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_11(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = None
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_12(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get(None)
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_13(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("XXPkgNameXX")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_14(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("pkgname")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_15(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PKGNAME")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_16(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) and not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_17(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) and not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_18(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_19(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_20(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_21(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = None
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_22(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.upper()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_23(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_24(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_25(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") and None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_26(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get(None) or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_27(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("XXFixedVersionXX") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_28(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("fixedversion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_29(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FIXEDVERSION") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_30(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=None, severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_31(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=None, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_32(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=None, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_33(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=None
    )


def x__to_cve_raw__mutmut_34(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        severity=normalized_severity, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_35(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, package=package, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_36(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, fix_version=fix_version
    )


def x__to_cve_raw__mutmut_37(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, )

mutants_x__to_cve_raw__mutmut['_mutmut_orig'] = x__to_cve_raw__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_1'] = x__to_cve_raw__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_2'] = x__to_cve_raw__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_3'] = x__to_cve_raw__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_4'] = x__to_cve_raw__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_5'] = x__to_cve_raw__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_6'] = x__to_cve_raw__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_7'] = x__to_cve_raw__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_8'] = x__to_cve_raw__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_9'] = x__to_cve_raw__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_10'] = x__to_cve_raw__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_11'] = x__to_cve_raw__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_12'] = x__to_cve_raw__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_13'] = x__to_cve_raw__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_14'] = x__to_cve_raw__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_15'] = x__to_cve_raw__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_16'] = x__to_cve_raw__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_17'] = x__to_cve_raw__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_18'] = x__to_cve_raw__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_19'] = x__to_cve_raw__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_20'] = x__to_cve_raw__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_21'] = x__to_cve_raw__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_22'] = x__to_cve_raw__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_23'] = x__to_cve_raw__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_24'] = x__to_cve_raw__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_25'] = x__to_cve_raw__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_26'] = x__to_cve_raw__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_27'] = x__to_cve_raw__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_28'] = x__to_cve_raw__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_29'] = x__to_cve_raw__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_30'] = x__to_cve_raw__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_31'] = x__to_cve_raw__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_32'] = x__to_cve_raw__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_33'] = x__to_cve_raw__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_34'] = x__to_cve_raw__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_35'] = x__to_cve_raw__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_36'] = x__to_cve_raw__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_cve_raw__mutmut['x__to_cve_raw__mutmut_37'] = x__to_cve_raw__mutmut_37 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_base_image__mutmut)
def _detect_base_image(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_orig(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_1(payload: dict[str, Any]) -> str | None:
    metadata = None
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_2(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") and {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_3(payload: dict[str, Any]) -> str | None:
    metadata = payload.get(None) or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_4(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("XXMetadataXX") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_5(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_6(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("METADATA") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_7(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = None
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_8(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") and {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_9(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get(None) or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_10(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("XXOSXX") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_11(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("os") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_12(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = None
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_13(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get(None)
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_14(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("XXFamilyXX")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_15(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_16(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("FAMILY")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_17(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = None
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_18(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get(None)
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_19(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("XXNameXX")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_20(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_21(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("NAME")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None


def x__detect_base_image__mutmut_22(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) or isinstance(name, str):
        return f"{family}:{name}"
    return None

mutants_x__detect_base_image__mutmut['_mutmut_orig'] = x__detect_base_image__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_1'] = x__detect_base_image__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_2'] = x__detect_base_image__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_3'] = x__detect_base_image__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_4'] = x__detect_base_image__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_5'] = x__detect_base_image__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_6'] = x__detect_base_image__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_7'] = x__detect_base_image__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_8'] = x__detect_base_image__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_9'] = x__detect_base_image__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_10'] = x__detect_base_image__mutmut_10 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_11'] = x__detect_base_image__mutmut_11 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_12'] = x__detect_base_image__mutmut_12 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_13'] = x__detect_base_image__mutmut_13 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_14'] = x__detect_base_image__mutmut_14 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_15'] = x__detect_base_image__mutmut_15 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_16'] = x__detect_base_image__mutmut_16 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_17'] = x__detect_base_image__mutmut_17 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_18'] = x__detect_base_image__mutmut_18 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_19'] = x__detect_base_image__mutmut_19 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_20'] = x__detect_base_image__mutmut_20 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_21'] = x__detect_base_image__mutmut_21 # type: ignore # mutmut generated
mutants_x__detect_base_image__mutmut['x__detect_base_image__mutmut_22'] = x__detect_base_image__mutmut_22 # type: ignore # mutmut generated
