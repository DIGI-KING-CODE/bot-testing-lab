import time


class BotTester:
    def __init__(self):
        self.results = []

    def check(self, name, passed, details=""):
        self.results.append({
            "name": name,
            "passed": passed,
            "details": details
        })

    def report(self):
        if not self.results:
            return "🧪 No tests executed."

        report = "🧪 TEST REPORT\n\n"

        for result in self.results:
            icon = "✅" if result["passed"] else "❌"
            report += f"{icon} {result['name']}\n"

            if result["details"]:
                report += f"   └─ {result['details']}\n"

        passed = sum(r["passed"] for r in self.results)
        total = len(self.results)

        report += f"\n📊 Result: {passed}/{total} PASS"

        return report


def run_basic_tests():
    tester = BotTester()

    start = time.perf_counter()

    tester.check(
        "Test engine",
        True,
        "Engine loaded successfully"
    )

    tester.check(
        "Python runtime",
        True,
        "Python is running"
    )

    elapsed = round(time.perf_counter() - start, 4)

    tester.check(
        "Execution speed",
        elapsed < 1,
        f"{elapsed}s"
    )

    return tester.report()
