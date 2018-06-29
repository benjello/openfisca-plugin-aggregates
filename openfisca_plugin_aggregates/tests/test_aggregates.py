# -*- coding: utf-8 -*-


from openfisca_france_data.tests import base
from openfisca_france_data.surveys import SurveyScenario
from openfisca_france_data.input_data_builders import get_input_data_frame
from openfisca_plugin_aggregates.aggregates import Aggregates


def create_survey_scenario(year = None):
    assert year is not None
    input_data_frame = get_input_data_frame(year)
    assert "wprm" in input_data_frame.columns
    survey_scenario = SurveyScenario().init_from_data_frame(
        input_data_frame = input_data_frame,
        tax_benefit_system = base.france_data_tax_benefit_system,
        year = year,
        )
    return survey_scenario


def test_aggregates(year = 2009):
    survey_scenario = create_survey_scenario(year)
    aggregates = Aggregates(survey_scenario = survey_scenario)
    aggregates.compute_aggregates()
    return aggregates.base_data_frame


if __name__ == '__main__':
    import logging
    log = logging.getLogger(__name__)
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    df = test_aggregates()
