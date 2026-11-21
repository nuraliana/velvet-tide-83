#!/usr/bin/env python3
"""VELMORA — The Floating Isles poster generator (copier).

Reproduces entry.png deterministically: the poster is stored in the repo
as entry.png and this program verifies its integrity (SHA-256, size,
PNG header, dimensions) before copying it to $MAKEFUN_OUTPUT_DIR.
"""
import hashlib
import os
import struct
import sys

EXPECTED_SHA256 = "3e48e7b06eab8b1a720ebd47dac39baf8198fe835b28747e5a72781fd0fe4ebb"
EXPECTED_SIZE = 267686
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
SOURCE_NAME = "entry.png"


def _fail(msg):
    print("error: " + msg, file=sys.stderr)
    sys.exit(1)


def _read_png_dimensions(data):
    if len(data) < 33:
        _fail("file too small to be a PNG")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        _fail("not a PNG file (bad signature)")
    if data[12:16] != b"IHDR":
        _fail("not a PNG file (missing IHDR)")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(src):
        _fail("source not found: " + src)
    with open(src, "rb") as fh:
        data = fh.read()
    if len(data) != EXPECTED_SIZE:
        _fail("size mismatch: got %d, expected %d" % (len(data), EXPECTED_SIZE))
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        _fail("sha256 mismatch: got " + digest)
    width, height = _read_png_dimensions(data)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        _fail("dimensions mismatch: got %dx%d" % (width, height))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        _fail("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, SOURCE_NAME)
    with open(out_path, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (out_path, len(data), digest))


if __name__ == "__main__":
    main()
