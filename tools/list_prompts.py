import json


def load_metadata(path="metadata/prompts.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def print_prompts(prompts, filter_tag=None):
    for i, prompt in enumerate(prompts, 1):
        tags = ", ".join(prompt["tags"])
        if filter_tag and filter_tag not in prompt["tags"]:
            continue
        print(f"[{i}] {prompt['title']}")
        print(f"    File: {prompt['file']}")
        print(f"    Lang: {prompt['language']} | Type: {prompt['type']}")
        print(f"    Tags: {tags}")
        print()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List available prompts with metadata.")
    parser.add_argument("--tag", help="Filter prompts by tag")
    args = parser.parse_args()

    prompts = load_metadata()
    print_prompts(prompts, args.tag)
