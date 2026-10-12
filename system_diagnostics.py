#!/usr/bin/env python3
"""
Nexus Dynamics - Core System & Environment Diagnostic Utility
Module: system_diagnostics.py
Classification: Internal Engineering Health Check (Rev 4.04)
"""

import sys
import time

# Ensure safe output encoding on various terminal environments
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass

def slow_print(text, delay=0.015, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

def fake_progress(task_name, duration=0.8):
    sys.stdout.write(f"[*] {task_name:<42} ")
    sys.stdout.flush()
    steps = 20
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        bar = "#" * i + "-" * (steps - i)
        sys.stdout.write(f"\r[*] {task_name:<42} [{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / steps)
    sys.stdout.write(" [OK]\n")
    sys.stdout.flush()

def print_banner():
    banner = r"""
 =========================================================================
   ___  ___  ___ _____ ___ _  _  ___     ___   ___ 
  | _ \/ _ \/ __|_   _|_ _| \| |/ __|   / _ \ / _ \
  |  _/ (_) \__ \ | |  | || .` | (_ |  | (_) | (_) |
  |_|  \___/|___/ |_| |___|_|\_|\___|   \___/ \___/ 
      >> NEXUS DYNAMICS // SYSTEM DIAGNOSTIC PROTOCOL v4.04 <<
 =========================================================================
    """
    print(banner)

def ask_question(question, options):
    print("\n" + "=" * 65)
    slow_print(question, delay=0.01)
    print("=" * 65)
    for idx, opt in enumerate(options, 1):
        print(f"  [{idx}] {opt}")
    print("-" * 65)
    
    while True:
        try:
            choice = input("Enter your selection (1-4): ").strip()
            if choice in ["1", "2", "3", "4"]:
                return int(choice)
            print("(!) Invalid telemetry input. Please choose 1, 2, 3, or 4.")
        except (KeyboardInterrupt, EOFError):
            print("\n\n[!] Interrupt detected. Exiting diagnostic.")
            sys.exit(0)

def main():
    print_banner()
    slow_print("[i] Initializing Nexus Infrastructure Health Probe...", delay=0.015)
    time.sleep(0.3)
    
    # Progress animation sequence
    fake_progress("Probing local heap allocations", duration=0.6)
    fake_progress("Scanning AST for steganographic payloads", duration=0.7)
    fake_progress("Evaluating developer curiosity index", duration=0.8)
    fake_progress("Bypassing imaginary quantum firewalls", duration=0.8)

    print("\n" + "*" * 65)
    slow_print("[!] NEXUS VERIFICATION INTERCEPT: ONBOARDING APTITUDE CHECK", delay=0.015)
    print("*" * 65)
    time.sleep(0.3)

    # Question 1
    q1 = "QUESTION 1: What is the scientifically proven cure for a SIGSEGV at 3 AM?"
    opts1 = [
        "Stare at the terminal until the bug fixes itself through quantum decay",
        "Six Snacks Hot Chai and Crispy Cutlets",
        "Rewrite the entire 10,000-line codebase in Brainf**k",
        "Blame compiler cosmic ray bit-flips and go to sleep"
    ]
    ans1 = ask_question(q1, opts1)
    if ans1 == 2:
        print("[+] Telemetry Match: Optimal neural fuel identified!")
    else:
        print("[~] Acceptable choice, but high-tier hackers usually prefer Six Snacks chai!")

    time.sleep(0.3)

    # Question 2
    q2 = "QUESTION 2: Which 'Cell' generates maximum freedom and community power?"
    opts2 = [
        "Mitochondria (the powerhouse of the biological cell)",
        "FOSS Cell GECT (the powerhouse of open-source innovation)",
        "Rechargeable Lithium-ion battery cell",
        "Cell B12 in a messy Excel spreadsheet"
    ]
    ans2 = ask_question(q2, opts2)
    if ans2 == 2:
        print("[+] Telemetry Match: Open-source spirit verified at 100%!")
    else:
        print("[~] Science is cool, but FOSS Cell GECT is legendary!")

    time.sleep(0.3)

    # Question 3
    q3 = "QUESTION 3: What is the most optimal next action in this treasure hunt?"
    opts3 = [
        "Spend 4 more hours staring at this python script looking for base64",
        "Rally the squad and head to Six Snacks for a delicious snack break",
        "Try typing 'sudo give_me_the_flag_please' in bash",
        "Contemplate why developers love Linux and free software"
    ]
    ans3 = ask_question(q3, opts3)
    if ans3 == 2:
        print("[+] Telemetry Match: Peak tactical decision making!")
    else:
        print("[~] Solid thought, though good food is always the winning move!")

    # Grand finale sequence
    print("\n")
    fake_progress("Synthesizing final diagnostic payload", duration=0.8)
    time.sleep(0.3)

    verdict = r"""
 =========================================================================
                      >>> DIAGNOSTIC COMPLETE <<<
           FLAG STATUS: [ 404 - ABSOLUTELY NO FLAG HERE, CHIEF! ]
 =========================================================================

  Caught you red-handed running mysterious Python scripts in the repo! ;)
  
  While this script contains ZERO puzzle flags, secret keys, or hints,
  it brings you two immutable truths of the hacker universe:

  [1] FREEDOM THRIVES IN OPEN SOURCE:
      A huge shout-out to FOSS Cell GECT! From Linux Install Fests to
      collaborative git repos, community-driven open source is the true
      heartbeat of engineering. Keep learning, keep sharing, and keep
      contributing to open code!

  [2] PEAK HACKING DEMANDS ELITE NOURISHMENT:
      A massive thank-you to our official sponsor: SIX SNACKS!
      When the puzzles get tricky and mental RAM runs low, step away
      from the screen, visit Six Snacks near GECT, and recharge with
      steaming kadum chaya, crispy cutlets, and good vibes.

  Now close this script, get back to the real hunt, and have fun!
 =========================================================================
    """
    print(verdict)

if __name__ == "__main__":
    main()
