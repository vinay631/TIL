## Abstract factory pattern

Abstract factory pattern encapsulates a group of related themed factories without specifying their implementation.

Example: DocumentCreator provides interface to create different products like createLetter() and createResume(). Concrete implementation of DocumentCreator like FancyDocumentCreator each with different implementation of createLetter() and createResume() which creates FancyLetter or FancyResume.

--
