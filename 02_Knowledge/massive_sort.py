import os
import shutil

ENTITIES_ROOT = r"C:\Anitigravity\02_Knowledge\entities"
DOMAINS = {
    "[AI]": r"C:\Anitigravity\02_Knowledge\03_AI_Data",
    "[Battery]": r"C:\Anitigravity\02_Knowledge\02_Battery",
    "[Semiconductor]": r"C:\Anitigravity\02_Knowledge\01_Semiconductor",
    "[Bio]": r"C:\Anitigravity\02_Knowledge\10_Bio_Healthcare",
    "[Aerospace]": r"C:\Anitigravity\02_Knowledge\06_Aerospace_Defense",
    "[Defense]": r"C:\Anitigravity\02_Knowledge\06_Aerospace_Defense",
    "[Smart Factory]": r"C:\Anitigravity\02_Knowledge\09_SmartFactory_Production",
    "[Digital Twin]": r"C:\Anitigravity\02_Knowledge\09_SmartFactory_Production",
    "[Mold]": r"C:\Anitigravity\02_Knowledge\09_SmartFactory_Production",
    "[Display]": r"C:\Anitigravity\02_Knowledge\07_Display_Comm",
    "[Communication]": r"C:\Anitigravity\02_Knowledge\07_Display_Comm",
    "[Energy]": r"C:\Anitigravity\02_Knowledge\25_Infrastructure",
    "[Infrastructure]": r"C:\Anitigravity\02_Knowledge\25_Infrastructure",
    "[Strategy]": r"C:\Anitigravity\02_Knowledge\04_Strategy_Mgmt",
    "[Economics]": r"C:\Anitigravity\02_Knowledge\04_Strategy_Mgmt",
    "[Enterprise]": r"C:\Anitigravity\02_Knowledge\04_Strategy_Mgmt",
    "[Robotics]": r"C:\Anitigravity\02_Knowledge\08_Robotics_Automation",
    "[Automation]": r"C:\Anitigravity\02_Knowledge\08_Robotics_Automation",
    "[Agriculture]": r"C:\Anitigravity\02_Knowledge\25_Infrastructure" # or a new folder if needed
}

def sort_entities():
    files = [f for f in os.listdir(ENTITIES_ROOT) if f.endswith(".md")]
    moved_count = 0
    for file in files:
        for tag, target_dir in DOMAINS.items():
            if file.startswith(tag):
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                src = os.path.join(ENTITIES_ROOT, file)
                dst = os.path.join(target_dir, file)
                
                # Check for existing
                if os.path.exists(dst):
                    # Keep larger
                    if os.path.getsize(src) > os.path.getsize(dst):
                        shutil.copy2(src, dst)
                    os.remove(src)
                else:
                    shutil.move(src, dst)
                
                moved_count += 1
                break
    print(f"Moved and Deduplicated {moved_count} entities to domain pillars.")

if __name__ == "__main__":
    sort_entities()
