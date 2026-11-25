import argparse
import shutil
import subprocess
import sys
import time

def parse_args():
    parser = argparse.ArgumentParser(
	description = "coffee_break_timer!!"
    )
    parser.add_argument(
	"-w",
	"--work",
	type = int,
	default = 5,
	help = "作業時間(分) default:25",
    )
    parser.add_argument(
	"-b",
	"--break-time",
	type = int,
	default = 5,
	help = "作業時間(秒) default:5",
    )
    parser.add_argument(
	"-c",
	"--cycles",
	type = int,
	default = 5,
	help = "繰り返すセット数 default:1",
    )
    return parser.parse_args()

def notify(title, message):
    sys.stdout.write("\a")
    sys.stdout.flash()

    if shutil.which("notify-send"):
	subprocess.run(["notify-send", title,message], check = False)

def countsown(label, minutes):
    total_sec = minutes * 60
    bar_length = 25
    sys.stdout.write("\033[?25l")
    for remaining in range(total_sec, 0, -1):
	mins, secs = divmod(remaining, 60)
	elapsed = total_sec - remaining
        filled = int(bar_length * elapsed / total_sec)
	bar = "\u2588" * filled + "\u2591" * (bar_length - filled)
	sys.stdout.write(f"[{label}]{bar}残り{mins:02d}")
	sys.stdout.flush()
	time.sleep(1)
    full_bar = "\u2588" * bar_length
    sys.stdout.write(f"\r[{label}]{full_bar}完了！ \n")
    sys.stdout.flush()

def main():
    args = parse_args()

    if args.work <= 0 or args.break_time <= 0 or args.cycle <= 0:
	print("エラー：すべての値は１以上の整数で指定してください。",file = sys.stderr)
	sys.exit(1)
    print(
	f"休憩開始（作業：{args.work}分 / 休憩：{args.break_time}分 X"
	f"{args.cycle}セット)"
    )

    try:
	for cycle in range(a, args.cycles + 1):
		print(f"\n---セット{cycle} / {args.cycles}---")
		countdown("作業中", args.work)
		notify(f"作業完了","{cycle}セット目の作業が終わりました。休憩しましょう！")
		if cycle < args.cycle
			countdown("休憩中", srgs.break_time)
			notify("休憩終了","休憩が終わりました。次の作業を始めましょう！")
	print(f"\nすべてのセットが完了しました!お疲れ様でした。"

    except KeyboardInterrupt:
	print("\n\nタイマーを中断しました。")
    finally:
	sys.stdout.write("\033[?25h")
	sys.stdout.flush()

if _name_ == "_main_":
    main()
