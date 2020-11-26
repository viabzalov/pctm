""" Context Sensitive Grammar Tests module """

from src.context_sensitive_grammar import ContextSensitiveGrammar

from src.utils import is_prime


def test_csg_manual(suite):
    """
    Checks that the given Context Sensitive Grammar generates the given word
    :param suite: Dictionary with test suite
        Dict['path'] - path to the file with the grammar
        Dict['word'] - word generated by the grammar
    :return: None
    """

    grammar = ContextSensitiveGrammar.from_txt(suite['path'])
    word = suite['word']

    assert (grammar.accepts(word) != tuple()) == is_prime(len(word))
