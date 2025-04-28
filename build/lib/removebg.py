#!/usr/bin/env python3
import argparse
from PIL import Image
import rembg
import sys

def remove_background(input_path, output_path):
    """Remove background from image using rembg"""
    try:
        input_image = Image.open(input_path)
        output_image = rembg.remove(input_image)
        output_image.save(output_path)
        print(f"Successfully removed background and saved to {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Remove background from images')
    parser.add_argument('--inputfile', '-i', required=True, help='Input image file path')
    parser.add_argument('--outputfile', '-o', required=True, help='Output image file path')
    
    args = parser.parse_args()
    
    remove_background(args.inputfile, args.outputfile)

if __name__ == "__main__":
    main()