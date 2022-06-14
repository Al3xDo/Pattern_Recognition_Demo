server:
	cd server && uvicorn app.main:app --reload
client:
	cd client && npm start

.PHONY: server client