from langchain_community.vectorstores import DeepLake


from schemas.model_schema import ModelSchema
from services.file_loader.file_loader import FileLoaderAndsplitter
from utils.model_selector import get_model

class VectorDb:
    """VectorDb class to create a vector database"""

    def create_vector_db_deeplake(
        self,
        db_path: str,
        chunk_size: int,
        chunk_overlap: int,
        overwrite: bool,
        documents: list,
        model: ModelSchema,
        encoding: str,
        sheet_name: str
    ) -> str:
        """Create a vector database using deeplake
        Args:
            db_path (str): Path to save the vector database
            chunk_size (int): Chunk size for the vector database
            chunk_overlap (int): Chunk overlap for the vector database
            overwrite (bool): Overwrite the existing vector database
            documents (list): List of documents to create the vector database
        Returns:
            str: Success message
        """

        embeddings = get_model(
            provider=model.provider,
            deployment=model.deployment,
            model=model.model_name,
            type=model.model_type,
            temperature=model.temperature,
        )

        try:

            docs_for_vector_db = []

            for doc in documents:
                docs_for_vector_db.extend(
                    FileLoaderAndsplitter().load_and_split_file(
                        file_path=doc,
                        text_splitting_name="recursive",
                        chunk_size=chunk_size,
                        chunk_overlap=chunk_overlap,
                        encoding=encoding,
                        sheet_name=sheet_name
                    )
                )

            DeepLake.from_documents(
                documents=docs_for_vector_db,
                embedding=embeddings,
                overwrite=overwrite,
                dataset_path=db_path,
            )

        except Exception as ex:
            raise Exception(f"Error in creating vector database: {str(ex)}")

        return "Vector database created successfully on path: " + db_path
