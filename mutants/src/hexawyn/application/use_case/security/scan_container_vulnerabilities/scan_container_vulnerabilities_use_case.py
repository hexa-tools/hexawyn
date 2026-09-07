from __future__ import annotations

from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort
from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
    ImageVulnerabilityScanPort,
)
from hexawyn.application.use_case.security.scan_container_vulnerabilities.command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.use_case.security.scan_container_vulnerabilities.response import (
    ScanContainerVulnerabilitiesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ScanContainerVulnerabilitiesUseCase:
    @_mutmut_mutated(mutants_xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut)
    def __init__(
        self,
        inventory_port: ImageInventoryPort,
        scan_port: ImageVulnerabilityScanPort,
    ) -> None:
        self._inventory = inventory_port
        self._scan = scan_port
    def xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut_orig(
        self,
        inventory_port: ImageInventoryPort,
        scan_port: ImageVulnerabilityScanPort,
    ) -> None:
        self._inventory = inventory_port
        self._scan = scan_port
    def xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut_1(
        self,
        inventory_port: ImageInventoryPort,
        scan_port: ImageVulnerabilityScanPort,
    ) -> None:
        self._inventory = None
        self._scan = scan_port
    def xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut_2(
        self,
        inventory_port: ImageInventoryPort,
        scan_port: ImageVulnerabilityScanPort,
    ) -> None:
        self._inventory = inventory_port
        self._scan = None

    @_mutmut_mutated(mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut)
    def execute(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_orig(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_1(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = None
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_2(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = None

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_3(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["XXimageXX"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_4(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["IMAGE"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_5(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = None
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_6(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(None):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_7(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = None
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_8(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(None)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_9(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                None
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_10(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "XXimageXX": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_11(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "IMAGE": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_12(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "XXstatusXX": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_13(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "STATUS": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_14(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["XXscan_statusXX"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_15(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["SCAN_STATUS"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_16(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "XXcve_countXX": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_17(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "CVE_COUNT": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_18(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=None,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_19(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=None,
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_20(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            summary=None,
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_21(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            total_images_scanned=len(scan_results),
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_22(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            summary=f"{len(scan_results)} images scanned",
        )

    def xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_23(
        self,
        command: ScanContainerVulnerabilitiesCommand,
    ) -> ScanContainerVulnerabilitiesResponse:
        images = self._inventory.list_running_images()
        unique_images: set[str] = {img["image"] for img in images}

        scan_results: list[dict[str, object]] = []
        for image_name in sorted(unique_images):
            result = self._scan.scan_image(image_name)
            scan_results.append(
                {
                    "image": image_name,
                    "status": result["scan_status"],
                    "cve_count": len(result["cves"]),
                }
            )

        return ScanContainerVulnerabilitiesResponse(
            findings=scan_results,  # type: ignore
            total_images_scanned=len(scan_results),
            )

mutants_xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut['_mutmut_orig'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut['xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut_1'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut['xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut_2'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['_mutmut_orig'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_1'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_2'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_3'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_4'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_5'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_6'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_7'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_8'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_9'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_10'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_11'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_12'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_13'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_14'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_15'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_16'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_17'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_18'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_19'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_20'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_21'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_22'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut['xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_23'] = ScanContainerVulnerabilitiesUseCase.xǁScanContainerVulnerabilitiesUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
