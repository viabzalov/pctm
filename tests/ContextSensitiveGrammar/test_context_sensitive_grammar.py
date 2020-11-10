""" Turing Machine Tests module """

from pyformlang import cfg

from src.context_sensitive_grammar import ContextSensitiveGrammar


def test_csg_manual(suite):
    """
    Checks that the given Context Sensitive Grammar generates the given word
    :param suite: Dictionary with test suite
        Dict['path'] - path to the file with the grammar
        Dict['word'] - word generated by the grammar
    :return: None
    """

    grammar = ContextSensitiveGrammar.from_txt(suite['path'])
    word = tuple([cfg.Terminal(x) for x in suite['word']])

    assert grammar.accepts(word)
