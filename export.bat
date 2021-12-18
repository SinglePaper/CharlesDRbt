@echo off
set /p ModelName=model name: 
if %ModelName% equ "": EXIT
python .\exporter_main_v2.py --input_type image_tensor --pipeline_config_path .\models\ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8\pipeline.config --trained_checkpoint_dir .\models\ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8\ --output_directory .\exported-models\%ModelName%