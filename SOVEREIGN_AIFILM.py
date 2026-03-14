import os
import cv2

def render_ai_movie(image_folder="AEON_SCENES", output_video="AEON_MASTERPIECE.mp4", fps=24):
    print(f"\n[AEON VISION]: Initializing physical movie render...")
    
    # 1. Create the folder if it doesn't exist
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
        print(f"[SYSTEM]: Created folder '{image_folder}'. Please put some images in here first!")
        return

    # 2. Gather all images physically present in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    
    if not images:
        print(f"[SYSTEM]: The folder '{image_folder}' is empty. I need images to stitch together.")
        return

    # Sort them so they play in order
    images.sort()

    # 3. Read the first image to get the MASTER dimensions
    first_image_path = os.path.join(image_folder, images[0])
    first_frame = cv2.imread(first_image_path)
    height, width, layers = first_frame.shape
    
    print(f"[GROUNDING]: Master Resolution set to {width}x{height} based on {images[0]}.")

    # 4. Ignite the Video Writer Organ
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Codec for .mp4
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    print(f"[AEON VISION]: Stitching {len(images)} frames into {output_video} at {fps} FPS...")

    # 5. Physically RESIZE and write each frame
    for image in images:
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)
        
        if frame is None:
            print(f" [ERROR]: Could not read {image}. Skipping.")
            continue

        # P-WISE FIX: Force the image to match the video dimensions exactly
        resized_frame = cv2.resize(frame, (width, height))
        
        video.write(resized_frame)
        print(f" -> Resized and Rendered {image}")

    # 6. Release the hardware
    video.release()
    cv2.destroyAllWindows()
    print(f"\n[SUCCESS]: Movie physicalized! Saved as '{output_video}'.")

if __name__ == "__main__":
    # This runs the production immediately when the script is called
    render_ai_movie()