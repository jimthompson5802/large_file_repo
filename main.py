def create_large_text_file(path: str, size_bytes: int) -> None:
    """Create a text file at `path` containing exactly `size_bytes` bytes.

    Uses ASCII 'a' characters to guarantee 1 byte per character in UTF-8.
    Existing file will be overwritten.
    """
    chunk = "a" * 8192  # 8 KiB chunk
    written = 0
    with open(path, "w", encoding="utf-8") as f:
        # write full chunks
        while written + len(chunk) <= size_bytes:
            f.write(chunk)
            written += len(chunk)
        # write remaining bytes
        remainder = size_bytes - written
        if remainder:
            f.write("a" * remainder)


def main():
    print("Hello from large-file-repo!")
    target = "my_large_text_file2.txt"
    target_size = 1000 * 1024  # 1000 KB = 1024000 bytes
    create_large_text_file(target, target_size)
    print(f"Created '{target}' with size {target_size} bytes.")


if __name__ == "__main__":
    main()
