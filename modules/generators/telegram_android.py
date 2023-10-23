import toml
import random

from .application import Application
from pathlib import Path

class TelegramAppAPI(Application):
    device_models = ['Samsung GT-I5510M', 'Samsung GT-I5800L', 'Samsung SCH-I559', 'Samsung SCH-i559', 'Samsung Behold II', 'Samsung GT-I9260', 'Samsung SM-A710XZ', 'Samsung GT-B9120', 'Samsung SCH-R880', 'Samsung SCH-R720', 'Samsung SGH-S730M', 'Samsung SHV-E270L', 'Samsung SAMSUNG-SGH-I927', 'Samsung SGH-I927', 'Samsung SCH-I699I', 'Samsung Samsung Chromebook 3', 'Samsung Samsung Chromebook Plus', 'Samsung kevin', 'Samsung Samsung Chromebook Plus (V2)', 'Samsung nautilus', 'Samsung Samsung Chromebook Pro', 'Samsung caroline', 'Samsung SPH-D600', 'Samsung SAMSUNG-SGH-I857', 'Samsung SCH-I510', 'Samsung SM-G1600', 'Samsung SM-G1650', 'Samsung GT-I5500B', 'Samsung GT-I5500L', 'Samsung GT-I5500M', 'Samsung GT-I5503T', 'Samsung GT-I5510L', 'Samsung SGH-T759', 'Samsung EK-GC100', 'Samsung GT-B9062', 'Samsung YP-GI2', 'Samsung SHW-M100S', 'Samsung archer', 'Samsung SM-A716S', 'Samsung SM-A015A', 'Samsung SM-A015AZ', 'Samsung SM-A015F', 'Samsung SM-A015G', 'Samsung SM-A015M', 'Samsung SM-A015T1', 'Samsung SM-A015U', 'Samsung SM-A015U1', 'Samsung SM-A015V', 'Samsung SM-S111DL', 'Samsung SM-A013F', 'Samsung SM-A013G', 'Samsung SM-A013M', 'Samsung SM-A022F', 'Samsung SM-A022G', 'Samsung SM-A022M', 'Samsung SM-A025A', 'Samsung SM-A025AZ', 'Samsung SM-A025F', 'Samsung SM-A025G', 'Samsung SM-A025M', 'Samsung SM-A025U', 'Samsung SM-A025U1', 'Samsung SM-A025V', 'Samsung SM-A105F', 'Samsung SM-A105FN', 'Samsung SM-A105G', 'Samsung SM-A105M', 'Samsung SM-A105N', 'Samsung SM-A102U', 'Samsung SM-A102U1', 'Samsung SM-A102W', 'Samsung SM-S102DL', 'Samsung SM-A102N', 'Samsung SM-A107F', 'Samsung SM-A107M', 'Samsung SM-A115A', 'Samsung SM-A115AP', 'Samsung SM-A115AZ', 'Samsung SM-A115F', 'Samsung SM-A115M', 'Samsung SM-A115U', 'Samsung SM-A115U1', 'Samsung SM-A115W', 'Samsung SM-A125F', 'Samsung SM-A125M', 'Samsung SM-A125N', 'Samsung SM-A125U', 'Samsung SM-A125U1', 'Samsung SM-S127DL', 'Samsung SM-A260F', 'Samsung SM-A260G', 'Samsung SC-02M', 'Samsung SCV46', 'Samsung SCV46-j', 'Samsung SCV46-u', 'Samsung SM-A205F', 'Samsung SM-A205FN', 'Samsung SM-A205G', 'Samsung SM-A205GN', 'Samsung SM-A205W', 'Samsung SM-A205YN', 'Samsung SM-A205U', 'Samsung SM-A205U1', 'Samsung SM-S205DL', 'Samsung SM-A202F', 'Samsung SM-A2070', 'Samsung SM-A207F', 'Samsung SM-A207M', 'Samsung SC-42A', 'Samsung SCV49', 'Samsung SM-A215U', 'Samsung SM-A215U1', 'Samsung SM-A215W', 'Samsung SM-S215DL', 'Samsung SM-A217F', 'Samsung SM-A217M', 'Samsung SM-A217N', 'Samsung SM-A226B', 'Samsung SM-A226B', 'Samsung SM-A300H', 'Samsung SM-A300F', 'Samsung SM-A300M', 'Samsung SM-A300XZ', 'Samsung SM-A300YZ', 'Samsung SM-A3000', 'Samsung SM-A300X', 'Samsung SM-A3009', 'Samsung SM-A300G', 'Samsung SM-A300F', 'Samsung SM-A3000', 'Samsung SM-A300YZ', 'Samsung SM-A300FU', 'Samsung SM-A300XU', 'Samsung SM-A300Y', 'Samsung SM-A320Y', 'Samsung SM-A013G', 'Samsung SM-A310F', 'Samsung SM-A310M', 'Samsung SM-A310X', 'Samsung SM-A310Y', 'Samsung SM-A310N0', 'Samsung SM-A320F', 'Samsung SM-A320FL', 'Samsung SM-A320X', 'Samsung SCV43', 'Samsung SCV43-j', 'Samsung SCV43-u', 'Samsung SM-A305F', 'Samsung SM-A305FN', 'Samsung SM-A305G', 'Samsung SM-A305GN', 'Samsung SM-A305GT', 'Samsung SM-A305N', 'Samsung SM-A305YN', 'Samsung SM-A307FN', 'Samsung SM-A307G', 'Samsung SM-A307GN', 'Samsung SM-A307GT', 'Samsung SM-A315F', 'Samsung SM-A315G', 'Samsung SM-A315N', 'Samsung SM-A325F', 'Samsung SM-A325M', 'Samsung SCG08', 'Samsung SM-A326B', 'Samsung SM-A326BR', 'Samsung SM-A326U', 'Samsung SM-A326U1', 'Samsung SM-A326W', 'Samsung SM-S326DL', 'Samsung SM-A405FM', 'Samsung SM-A405FN', 'Samsung SM-A405S', 'Samsung SM-A3050', 'Samsung SM-A3051', 'Samsung SM-A3058', 'Samsung SC-41A', 'Samsung SCV48', 'Samsung SM-A415F', 'Samsung SM-A4260', 'Samsung SM-A426B', 'Samsung SM-A426N', 'Samsung SM-A426U', 'Samsung SM-A426U1', 'Samsung SM-A500H', 'Samsung SM-A500F', 'Samsung SM-A500G', 'Samsung SM-A500M', 'Samsung SM-A500XZ', 'Samsung SM-A5000', 'Samsung SM-A500X', 'Samsung SM-A5009', 'Samsung SM-A5000', 'Samsung SM-A500YZ', 'Samsung SM-A500FU', 'Samsung SM-A500Y', 'Samsung SM-A500W', 'Samsung SM-A500K', 'Samsung SM-A500L', 'Samsung SM-A500F1', 'Samsung SM-A500S', 'Samsung SM-A510Y', 'Samsung SM-A510F', 'Samsung SM-A510M', 'Samsung SM-A510X', 'Samsung SM-A510Y', 'Samsung SM-A5108', 'Samsung SM-A510K', 'Samsung SM-A510L', 'Samsung SM-A510S', 'Samsung SM-A510Y', 'Samsung SM-A5100', 'Samsung SM-A5100X', 'Samsung SM-A510XZ', 'Samsung SM-A520F', 'Samsung SM-A520X', 'Samsung SM-A520W', 'Samsung SM-A520K', 'Samsung SM-A520L', 'Samsung SM-A520S', 'Samsung SM-A505F', 'Samsung SM-A505FM', 'Samsung SM-A505FN', 'Samsung SM-A505G', 'Samsung SM-A505GN', 'Samsung SM-A505GT', 'Samsung SM-A505N', 'Samsung SM-A505U', 'Samsung SM-A505U1', 'Samsung SM-A505W', 'Samsung SM-A505YN', 'Samsung SM-S506DL', 'Samsung SM-A5070', 'Samsung SM-A507FN', 'Samsung SM-A515F', 'Samsung SM-A515U', 'Samsung SM-A515U1', 'Samsung SM-A515W', 'Samsung SM-S515DL', 'Samsung SC-54A', 'Samsung SCG07', 'Samsung SM-A5160', 'Samsung SM-A516B', 'Samsung SM-A516N', 'Samsung SM-A516U', 'Samsung SM-A516U1', 'Samsung SM-A516V', 'Samsung SM-A525F', 'Samsung SM-A5260', 'Samsung SM-A526B', 'Samsung SM-A526N', 'Samsung SM-A526U', 'Samsung SM-A526U1', 'Samsung SM-A526W', 'Samsung SM-A600AZ', 'Samsung SM-A600A', 'Samsung SM-A600T1', 'Samsung SM-A600P', 'Samsung SM-A600T', 'Samsung SM-A600U', 'Samsung SM-A600F', 'Samsung SM-A600FN', 'Samsung SM-A600G', 'Samsung SM-A600GN', 'Samsung SM-A600N', 'Samsung SM-A605F', 'Samsung SM-A605FN', 'Samsung SM-A605G', 'Samsung SM-A605GN', 'Samsung SM-A6050', 'Samsung SM-A6060', 'Samsung SM-A606Y']
    sdk_versions = ["11 R? (30)", "10 Q (29)", "9 P (28)", "8 O (27)"]
    app_versions = ["8.8.3", "8.8.4", "8.8.5"]

    lang_pack = "android"

    path: Path = Path(__file__).parent.parent.parent
    
    if not path.joinpath("config.toml").exists():
        path = path.parent.parent

    if path.joinpath("config.toml").exists():

        with open(path.joinpath("config.toml")) as file:
            config = toml.load(file)["sessions"]

        api_id = config["api_id"]
        api_hash = config["api_hash"]
    
    else:
        api_id = 6
        api_hash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

    @staticmethod
    def app_version() -> str:
        return random.choice(TelegramAppAPI.app_versions)

    @staticmethod
    def device() -> str:
        return random.choice(TelegramAppAPI.device_models)

    @staticmethod
    def sdk() -> str:
        return random.choice(TelegramAppAPI.sdk_versions)
