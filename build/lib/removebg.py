#!/usr/bin/env python3
import argparse
import sys

def check_dependencies():
    """Check for required dependencies"""
    try:
        from PIL import Image
        import rembg
        import onnxruntime
    except ImportError as e:
        print(f"Error: Missing required dependency - {str(e)}", file=sys.stderr)
        print("Please install dependencies with: pip install rembg pillow onnxruntime", file=sys.stderr)
        sys.exit(1)

def remove_background(input_path, output_path):
    """Remove background from image using rembg"""
    try:
        from PIL import Image
        import rembg
        
        input_image = Image.open(input_path)
        output_image = rembg.remove(input_image)
        
        # Ensure output is PNG for transparency support
        if not output_path.lower().endswith('.png'):
            print("Warning: Output format changed to PNG to preserve transparency", file=sys.stderr)
            output_path = output_path.rsplit('.', 1)[0] + '.png'
            
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
    
    check_dependencies()
    remove_background(args.inputfile, args.outputfile)

if __name__ == "__main__":
    main()