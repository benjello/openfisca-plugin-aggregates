# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014, 2015 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from openfisca_france_data.input_data_builders import get_input_data_frame
from openfisca_france_data.surveys import SurveyScenario
from openfisca_plugin_aggregates.aggregates import Aggregates


def create_survey_scenario(year = None, reform = None):
    assert year is not None
    if reform is not None :
        log.warning("="*10 + "Is working in reform mode, take care when compare to true aggregates"+ "="*10)
    input_data_frame = get_input_data_frame(year)
    survey_scenario = SurveyScenario().init_from_data_frame(
        input_data_frame = input_data_frame,
        reform = reform,
        used_as_input_variables = ['salaire_imposable', 'cho', 'rst', 'age_en_mois'],
        year = year,
        )

    return survey_scenario


def test_aggregates(year = None, reform = None):
    '''
    test aggregates value with data
    :param year: year of data and simulation to test agregates
    :param reform: optional argument, put an openfisca_france.refoms object, default None
    '''
    assert year is not None
    survey_scenario = create_survey_scenario(year, reform)
    aggregates = Aggregates(survey_scenario = survey_scenario)
    aggregates.compute()
    print aggregates.aggr_frame
    return aggregates


if __name__ == '__main__':
    from openfisca_france.reforms import allocations_familiales_imposables as reform
    import logging
    log = logging.getLogger(__name__)
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    aggregates = test_aggregates(year = 2009, reform = reform)
 #   df = aggregates.aggr_frame