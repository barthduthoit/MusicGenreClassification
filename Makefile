init:
	pip install -r requirements.txt

data:
	./init.sh

clean:
	rm -rf data/
	rm logfile.log
