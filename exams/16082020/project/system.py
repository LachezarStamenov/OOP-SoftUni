from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)

        except IndexError:
            return "Software cannot be installed"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)

        except IndexError:
            return "Software cannot be installed"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} /" \
               f" {sum([h.memory for h in System._hardware])}\n" \
               f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} /" \
               f" {sum([h.capacity for h in System._hardware])}"

    @staticmethod
    def system_split():
        output = ""

        for hardware in System._hardware:
            express_software_installed = [sw for sw in hardware.software_components if sw.software_type == "Express"]
            light_software_installed = [sw for sw in hardware.software_components if sw.software_type == "Light"]
            memory_usage = sum([sw.memory_consumption for sw in hardware.software_components])
            capacity_usage = sum([sw.capacity_consumption for sw in hardware.software_components])
            software_components_names = [sw.name for sw in
                                         hardware.software_components] if hardware.software_components else "None"

            output += f"Hardware Component - {hardware.name}\n"
            output += f"Express Software Components: {len(express_software_installed)}\n"
            output += f"Light Software Components: {len(light_software_installed)}\n"
            output += f"Memory Usage: {memory_usage} / {hardware.memory}\n"
            output += f"Capacity Usage: {capacity_usage} / {hardware.capacity}\n"
            output += f"Type: {hardware.hardware_type}\n"
            output += f"Software Components: {', '.join(software_components_names)}\n"

        return output.strip()