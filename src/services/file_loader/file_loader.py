from langchain_community.document_loaders import (
    TextLoader,
    UnstructuredExcelLoader,
    PyPDFLoader,
    Docx2txtLoader,
)
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
import os


class FileLoaderAndsplitter:
    """FileLoaderAndsplitter class to load and split files"""

    def _txt_loader_and_splitting(
        self, file_path, text_splitting, encoding: str = "utf-8"
    ):
        """Return the splitted documents from the txt file path."""

        loader = TextLoader(file_path, encoding=encoding)
        documents = loader.load()

        return text_splitting.split_documents(documents)

    def _pdf_loader_and_splitting(self, file_path, text_splitting):
        """Return the splitted documents from the pdf file path."""

        loader = PyPDFLoader(file_path)
        documents = loader.load()

        return text_splitting.split_documents(documents)

    def _docx_loader_and_splitting(self, file_path, text_splitting):
        """Return the splitted documents from the docx file path."""

        loader = Docx2txtLoader(file_path)
        documents = loader.load()

        return text_splitting.split_documents(documents)

    def _xlsx_loader_and_splitting(self, file_path, text_splitting, sheet_name=None):
        """Return the splitted documents from the excel file path."""

        if sheet_name != None:
            loader = UnstructuredExcelLoader(file_path, mode="elements")
            documents = loader.load()

            return text_splitting.split_documents(documents)
        else:
            raise Exception("Sheet name is not provided!")

    def _get_text_splitter(self, text_splitting_name, chunk_size, chunk_overlap):
        """Return the text splitting method based on the name."""

        match text_splitting_name:
            case "recursive":
                text_splitting = RecursiveCharacterTextSplitter(
                    separators=["\n\n\n", "\n\n", " ", ""],
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                    strip_whitespace=True,
                )
            case "_":
                text_splitting = CharacterTextSplitter(
                    chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator="\n\n"
                )

        return text_splitting

    def load_and_split_file(
        self,
        file_path,
        text_splitting_name,
        chunk_size,
        chunk_overlap,
        encoding: str = "utf-8",
        sheet_name=None,
    ):
        """Return the splitted documents from the file path.
        Args:
            file_path (str): Path of the file
            text_splitting_name (str): Name of the text splitting method [recursive, _]
                default: CharacterTextSplitter
            chunk_size (int): Chunk size for the text splitting
            chunk_overlap (int): Chunk overlap for the text splitting
            encoding (str): Encoding of the file
            sheet_name (str): Sheet name for the excel file

        Returns:
            list: List of splitted documents"""

        text_splitting_name = self._get_text_splitter(
            text_splitting_name, chunk_size, chunk_overlap
        )

        if os.path.exists(file_path):

            extension = os.path.splitext(file_path)[1]

            if extension == ".pdf":
                return self._pdf_loader_and_splitting(file_path, text_splitting_name)

            elif extension == ".docx" or extension == ".doc":
                return self._docx_loader_and_splitting(file_path, text_splitting_name)

            elif extension == "xlsx":
                return self._xlsx_loader_and_splitting(
                    file_path, text_splitting_name, sheet_name
                )

            elif extension == ".txt":
                return self._txt_loader_and_splitting(
                    file_path, text_splitting_name, encoding=encoding
                )

            else:
                raise Exception("File type is not supported!")
        else:
            raise Exception("File path is not valid!")
