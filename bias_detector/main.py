from bias_detector.config import (
    get_scan_patterns,
    load_exclude_terms,
    get_cutoff,
)
from bias_detector.embeddings import load_embeddings
from bias_detector.gender_axis import load_gender_axis
from bias_detector.scanner import get_files_from_patterns, scan_files


def main():
    print("🔍 Loading GloVe embeddings...")
    embedding = load_embeddings()

    print("🧭 Computing gender direction...")
    gender_direction = load_gender_axis(embedding)

    print("📂 Resolving scan paths...")
    patterns = get_scan_patterns()
    files = get_files_from_patterns(patterns)
    print(f"📄 Found {len(files)} file(s) to scan.")

    exclude_terms = load_exclude_terms()
    cutoff = get_cutoff()

    flagged = scan_files(
        files,
        exclude_terms,
        embedding,
        gender_direction,
        cutoff,
    )

    if flagged:
        print("\n🚨 Biased terms detected:")
        for item in flagged:
            print(item)
        print("::set-output name=found::true")
        print(f"::set-output name=report::{chr(10).join(flagged)}")
        exit(1)
    else:
        print("✅ No strongly gender-biased terms detected.")
        print("::set-output name=found::false")
        print("::set-output name=report::")
        exit(0)


if __name__ == "__main__":
    main()
