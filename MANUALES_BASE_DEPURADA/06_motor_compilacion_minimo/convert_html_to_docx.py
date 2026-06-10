import os
import pypandoc
import glob

# Ensure pandoc is downloaded
try:
    pypandoc.get_pandoc_version()
except OSError:
    print("Downloading pandoc...")
    pypandoc.download_pandoc()

dist_folder = 'dist'
html_files = glob.glob(os.path.join(dist_folder, 'gem-manual-*.html'))

for html_path in html_files:
    docx_path = html_path.replace('.html', '.docx')
    print(f"Converting {html_path} to {docx_path}...")
    try:
        # Convert using pypandoc
        # The working directory for Pandoc needs to be the root folder so that relative paths like "../assets/iconos" resolve correctly from within 'dist'
        # Actually, in the HTML, they are just paths. Pandoc resolves them relative to the input file's directory by default.
        # So '../assets/iconos/...' relative to 'dist/' resolves to 'assets/iconos/...' which is correct.
        pypandoc.convert_file(
            html_path, 
            'docx', 
            outputfile=docx_path,
            extra_args=['--resource-path=dist']
        )
        print(f"Converted successfully: {docx_path}")
    except Exception as e:
        print(f"Failed to convert {html_path}: {e}")
