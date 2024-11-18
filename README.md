# AI-app

## API Végpontok

### Válasz végpont

- **Végpont:** `/api/answer`
- **Módszer:** `POST`
- **Leírás:** Ez a végpont feldolgozza a kérdést és AI által generált választ ad vissza.
- **Kérelem Törzse:**
    - `prompt` (string): Az AI modell számára adott prompt a LangSmith hub-ból.
    - `model` (object): Az AI modell konfigurációja.
      - `name` (string): A modell neve.
      - `model_type` (string): A modell típusa.
      - `deployment` (string|null): A modell telepítése.
      - `provider` (string): A szolgáltató neve.
      - `temperature` (number): A válasz generálásának hőmérséklete.
    - `tools` (array): Eszközök konfigurációja.
      - `name` (string): Az eszköz neve.
      - `vector_db_path` (string): A vektor adatbázis elérési útja.
      - `required` (bool): Az eszköz szükségessége.
      - `model` (object): Az eszköz modell konfigurációja.
        - `model_name` (string): A modell neve.
        - `model_type` (string): A modell típusa.
        - `deployment` (string|null): A modell telepítése.
        - `provider` (string): A szolgáltató neve.
      - `search_kwargs` (object): Keresési paraméterek.
        - `k` (number): A keresési találatok száma.
        - `threshold` (number): A keresési küszöbérték.
        - `search_type` (string): A keresés típusa.
      - `engine` (string): A keresőmotor neve.
    - `user_input` (string): A felhasználó kérdése.


```json
{
  "prompt": "kérdés",
  "user_input": "Hogy vagy",
  "model": {
    "name": "gpt-4o-mini",
    "model_type": "chat",
    "deployment": null,
    "provider": "openai",
    "temperature": 0
  },
  "tools": [
    {
      "name": "retriver_tool",
      "vector_db_path": "deeplake_databases/deeplake_db_pdf",
      "required": true,
      "model": {
        "model_name": "text-embedding-3-large",
        "model_type": "embedding",
        "deployment": null,
        "provider": "openai"
      },
      "search_kwargs": {
        "k": 5,
        "threshold": 0.5,
        "search_type": "similarity"
      }
    },
    {
      "name": "web_search_tool",
        "engine": "google"
    }
  ]
}
```

- **Válaszok:**
    - `200 OK`: Visszaadja az AI által generált választ.
    - `500 Internal Server Error`: Ha hiba történt a kérés feldolgozása során.


### Vektor adatbázis végpont

- **Végpont:** `/api/vector_db/create`
- **Módszer:** `POST`
- **Leírás:** Ez a végpont létrehoz egy vektordatabase-t.
- **Kérelem Törzse:**
    - `db_type` (string): A vektordatabase típusa [deeplake].
    - `db_path` (string): Az adatbázis elérési útja.
    - `chunk_size` (int): A darabok mérete.
    - `chunk_overlap` (int): Az átfedés a darabok között.
    - `overwrite` (bool): Felülírja-e a meglévő adatbázist.
    - `documents` (list): Az adatbázishoz hozzáadandó dokumentumok.
    - `model` (string): A használni kívánt modell.
    - `file_load_encoding` (string): A betöltendő fájl kódolása.
    - `sheet_name` (string): A lap neve (ha alkalmazható).
- **Válaszok:**
    - `200 OK`: Ha a vektordatabase sikeresen létrejött.
    - `400 Bad Request`: Ha a vektordatabase típusa nem támogatott.
    - `500 Internal Server Error`: Ha hiba történt a kérés feldolgozása során.

```json
{
  "db_path": "deeplake_databases/deeplake_db_docx",
  "db_type": "deeplake",
  "documents": [
    "files/cv.docx"
  ],
  "sheet_name":"pharagraph-dataset",
  "chunk_size": 3000,
  "chunk_overlap": 200,
  "overwrite": true,
  "model": {
    "model_name": "text-embedding-3-large",
    "provider": "openai",
    "model_type":"embedding"
  }
}
```


## Használt dokumentációk és szolgáltatások:
- https://python.langchain.com/docs/how_to/migrate_agent/
- https://langchain-ai.github.io/langgraph/#example
- https://python.langchain.com/docs/integrations/tools/serpapi/
- https://serpapi.com/manage-api-key
- https://smith.langchain.com/