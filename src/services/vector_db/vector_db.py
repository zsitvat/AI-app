from langchain_community.vectorstores import DeepLake
from langchain.chat_models import init_chat_model

from schemas.model_schema import ModelSchema
from services.file_loader.file_loader import FileLoaderAndsplitter


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

        embeddings = init_chat_model(
            model_name=model.model_name,
            model_type=model.model_type,
            provider=model.provider,
            temperature=model.temperature,
        )

        try:

            docs = FileLoaderAndsplitter.load_and_split_file(
                file_path=documents,
                text_splitting_name="recursive",
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                encoding=encoding,
            )

            vectorstore = DeepLake.from_documents(
                docs,
                embeddings,
                dataset_path=db_path,
                overwrite=overwrite,
            )

        except Exception as ex:
            raise Exception(f"Error in creating vector database: {str(ex)}")

        return "Vector database created successfully on path: " + db_path
