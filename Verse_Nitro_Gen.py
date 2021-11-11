import time
import os
import random
import string
import ctypes

# Imports:
# pip install requests
# pip install discord_webhook

try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(f"Module discord_webhook is not installed, to install run pip install discord_webhook'\nPress enter to exit...")
    exit()
try:
    import requests
except ImportError:
    input(f"Module requests is not installed, to install run pip install requests'\nPress enter to exit...")
    exit()


class VerseGen:
    def __init__(self):
        self.fileName = "Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("VerseGenerator - Made by DraKen")
        else:
            print(f"""██╗░░░██╗███████╗██████╗░░██████╗███████╗
██║░░░██║██╔════╝██╔══██╗██╔════╝██╔════╝
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░█████╗░░
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██╔══╝░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝\a""")


        print("\nVerse Nitro Generator - Made by DraKen")
        num = int(input("\nHow Many Codes Do You Want To Generate And Check: "))

        url = input("\nDo you want to use a webhook ? (Press Enter to skip)  ")
        webhook = url if url != "" else None

        valid = []
        invalid = 0

        for i in range(num):
            try:
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"VerseGenerator  - {len(valid)} Valid - {invalid} Invalid")
                print("")
            else:
                print(f'VerseGenerator - {len(valid)} Valid | {invalid} Invalid')

        print(f"""
Results:
Valid: {len(valid)}
Invalid: {invalid}
Valid Codes: {', '.join(valid )}""")

        input("\nPress Enter to exit...")

    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Wait, Generating for you")

            start = time.time()

            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))

                file.write(f"https://discord.gift/{code}\n")

            print(f"Generated {amount} codes.\n")

    def fileChecker(self, notify = None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url)

                if response.status_code == 200:
                    print(f" Valid | {nitro} ")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"Valid Nito Code detected! @everyone \n{nitro}"
                        ).execute()
                    else:
                        break 

                else:
                    print(f" Invalid | {nitro} ")
                    invalid += 1

        return {"valid" : valid, "invalid" : invalid}

    def quickChecker(self, nitro, notify = None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"Valid Nito Code detected: \n{nitro}"
                ).execute()

            return True

        else:
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Gen = VerseGen()
    Gen.main()
