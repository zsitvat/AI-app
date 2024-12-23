from langchain_community.vectorstores import DeepLake
from langchain_core.embeddings import Embeddings
import logging


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
        embeddings_model: Embeddings,
        encoding: str,
        sheet_name: str,
    ) -> str:
        """Create a vector database using deeplake
        Args:
            db_path (str): Path to save the vector database
            chunk_size (int): Chunk size for the vector database
            chunk_overlap (int): Chunk overlap for the vector database
            overwrite (bool): Overwrite the existing vector database
            documents (list): List of documents to create the vector database
            model (ModelSchema): Model schema
            encoding (str): Encoding of the txt file
            sheet_name (str): Sheet name for the excel file
        Returns:
            str: Success message
        """

        logging.getLogger("logger").debug("Creating vector database using deeplake")

        if not isinstance(embeddings_model, Embeddings):
            raise TypeError("The model is not of type 'Embeddings'")

        try:

            docs_for_vector_db = []

            for doc in documents:
                docs_for_vector_db.extend(
                    FileLoaderAndsplitter().load_and_split_file(
                        file_path=doc,
                        text_splitter_name="recursive",
                        chunk_size=chunk_size,
                        chunk_overlap=chunk_overlap,
                        encoding=encoding,
                        sheet_name=sheet_name,
                    )
                )

            DeepLake.from_documents(
                documents=docs_for_vector_db,
                embedding=embeddings_model,
                overwrite=overwrite,
                dataset_path=db_path,
            )

            logging.getLogger("logger").info(
                f"Vector database created successfully at {db_path}."
            )

            return f"Vector database created successfully on path: {db_path}"

        except Exception as ex:
            logging.getLogger("logger").error(
                f"Error in creating vector database: {str(ex)}"
            )
            raise ex
