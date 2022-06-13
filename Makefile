start-server:
	cd server && uvicorn app.main:app --reload
start-client:
	cd client && npm start

.PHONY: start-server start-client