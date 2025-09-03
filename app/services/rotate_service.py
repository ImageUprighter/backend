from ai.upright_faces import rotate_faces_in_folder  # assuming AI logic is exposed here

async def rotateImages(input_folder: str, size: tuple = None):
    output_folder = input_folder + "_rotated"
    await rotate_faces_in_folder(input_folder, output_folder, size)  # You can tweak this

    return output_folder
