import timeit
import typing as t
import importlib

import pandas as pd
from pyramid.paster import bootstrap
from pyramid.request import Request
from sqlalchemy.orm import Session


def to_df(
    query,
    *,
    pivot: dict = {},
    debug: bool = False,
):
    '''
    NOTE: This currently only works with query that has defined output
    with with_entities()
    '''
    if debug:
        start = timeit.default_timer()

    df = pd.read_sql(
        query.statement,
        query.session.bind,
    )
    if pivot:
        df = df.pivot(**pivot)

        df.index.name = 'time'
        df = df[df.index.notnull()]
        del df.columns.name

    if debug:
        stop = timeit.default_timer()
        print(f'Convert to DF: {(stop - start):.6f} seconds')

    return df


# def fill_calculated_features(line_uid: str, inputs):
#     """
#     Fill current data of calculated features.

#     :param line_uid: UID of fiber line
#     :param inputs: query results of tag having tag_name and value
#     :returns: list of filled tag
#     """
#     rows = [i._asdict() for i in inputs]
#     line_resource = LineResource(line_uid)
#     (
#         calculated_features, build_features
#     ) = line_resource.get_calculated_features()

#     if build_features is None:
#         return rows

#     df = pd.DataFrame(rows)
#     df = df.pivot(columns='tag_name', values='value')
#     df = df.fillna(method="ffill").fillna(method="bfill").tail(1)

#     df = build_features(df)
#     df = df.where(pd.notnull(df), None)
#     for row in rows:
#         if row['tag_name'] in calculated_features:
#             row['value'] = df[row['tag_name']].values[0]

#     return rows


# def create_db_session(config: str) -> t.Tuple[Request, Session]:
#     if not config.endswith((
#         'development.ini',
#         'production.ini',
#         'test.ini',
#     )):
#         raise ValueError('Invalid config path')
#     with bootstrap(config) as app:
#         return app['request'], app['request'].find_service(Session)
