from fregepoc.repositories.analyzers import AnalyzerFactory
from fregepoc.repositories.analyzers.generic import GenericAnalyzer
from fregepoc.repositories.constants import ProgrammingLanguages
from fregepoc.repositories.utils.analyzers import FileInformationDict


@AnalyzerFactory.register(ProgrammingLanguages.JAVA)
class JavaAnalyzer(GenericAnalyzer[FileInformationDict]):
    pass
