RESIZE = python3 util/resize.py


default:
	@echo '  >> make {resize}'

resize:
	./init_genre_dir.sh '${dir_path}_${factor}'
	 ${RESIZE} $(factor) $(dir_path)
