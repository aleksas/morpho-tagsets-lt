#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main
from random import shuffle
import multext_east_jablonskis_convertor.multext_east_jablonskis as mej

noun_cases = [
    ('Lietuvai', 'Npfsdng', ['dkt.', 'tikr.', 'mot.', 'vns.', 'N.']),
    ('vasarą', 'Ncfsan-', ['dkt.', 'mot.', 'vns.', 'G.']),
    ('bankucheno', 'Nnmsgn-', ['dkt.', 'vyr.', 'vns.', 'K.']), # !DOC ISSUE: bankuchenas > bankucheno
]

verb_cases = [
    ('rezervuoju', 'Vgmp1s--n--ni-', ['vksm.', 'asm.', 'tiesiog.', 'es.', 'vns.', '1.']),
    ('paliktu', 'Vgps-smpnnin-p', ['vksm.', 'dlv.', 'neveik.', 'būt.', 'nelygin.', 'vyr.', 'vns.', 'Įn.']),
    ('bėgte', 'Vgb-----n--n--', ['vksm.', 'būdn.']),
]

adjective_cases = [
    ('svarbu', 'Agpn--n', ['bdv.', 'nelygin.', 'bev.']),
    ('gražiausius', 'Agsmpan', ['bdv.', 'aukšč.', 'vyr.', 'dgs.', 'G.']),
    ('biednas', 'Anpmsnn', ['bdv.', 'nelygin.', 'vyr.', 'vns.', 'V.']),
]

pronoun_cases = [
    ('visokie', 'Pgmpin', ['įv.', 'vyr.', 'dgs.', 'Įn.']), # !DOC ISSUE: visoks > visokie
    ('man', 'Pg-sdn', ['įv.', 'vns.', 'N.']),
    ('toooks', 'Pgmsnn', ['įv.', 'vyr.', 'vns.', 'V.']), # !DOC ISSUE: Pnmsnn > Pgmsnn, toooks > toks?
]

numeral_cases = [
    ('penkiom', 'Mcf-iln', ['sktv.', 'raid.', 'kiek.', 'mot.', 'Įn.']),
    ('penkiom', 'Mcf-dln', ['sktv.', 'raid.', 'kiek.', 'mot.', 'N.']),
    ('10', 'M----d-', ['sktv.', 'arab.']),
    ('pem', 'Mn-----', ['sktv.']),
]

adverb_cases = [
    ('apskritai', 'Rgp', ['prv.', 'nelygin.']),
    ('geriau', 'Rgc', ['prv.', 'aukšt.']),
]

preposition_cases = [
    ('su', 'Sgi', ['prl.', 'Įn.']),
    ('po','Sgg', ['prl.', 'K.']),
    ('po','Sga', ['prl.', 'G.']),
    ('po','Sgi', ['prl.', 'Įn.']),
]

conjunction_cases = [
    ('būtent', 'Cg', ['jng.']),
    ('ir', 'Cg', ['jng.']),
]

tests = [
    (noun_cases, mej.noun),
    (verb_cases, mej.verb),
    (adjective_cases, mej.adjective),
    (pronoun_cases, mej.pronoun),
    (numeral_cases, mej.numeral),
    (adverb_cases, mej.adverb),
    (preposition_cases, mej.preposition),
    (conjunction_cases, mej.conjunction)
]

class SimpleTestCase(TestCase):
    def test_1(self):
        for cases, category in tests:
            for _, multext, jablonskis_tags in cases:
                tags = list(mej.get_jablonskis_tags(multext))
                self.assertEqual(jablonskis_tags, tags)

                category_tag = list(category[0].values())[0]
                self.assertIn(category_tag, tags)
    
    def test_2(self):
        for cases, _ in tests:
            for _, _, jablonskis_tags in cases:
                shffled_jablonskis_tags = list(jablonskis_tags)
                shuffle(shffled_jablonskis_tags)
                mej.sort_jablonskis_tags(shffled_jablonskis_tags)

                self.assertEqual(jablonskis_tags, shffled_jablonskis_tags)

if __name__ == '__main__':
    main()