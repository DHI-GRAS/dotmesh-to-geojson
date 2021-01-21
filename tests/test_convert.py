import textwrap

import pytest


def pseudo_dotmesh_ok():
    return textwrap.dedent(
        """100079 1000 10 LONG/LAT
        1	        9.5552751717	       55.7048492992	   -1.10263693332672	1
        2	          9.55555483	       55.7070180551	   -1.07409691810608	1
        3	        9.5556373282	       55.7012631915	   -2.04877686500549	1
        4	        9.5562467073	       55.6990617921	   -1.87206864356995	1
        5	        9.5564396797	       55.7088381724	   -1.04766762256622	1
        6	        9.5570337145	       55.7043310442	   -1.21277117729187	1
        7	        9.5572178675	       55.7015625199	   -1.95995485782623	1
        8	        9.5574468908	        55.710631561	    -1.0869619846344	1
        9	        9.5587127447	       55.6982698091	   -1.49362623691559	1
        10	        9.5592156924	       55.7041647203	   -1.60801577568054	1
        38031 4 25
        1 178 179 181 0
        2 3912 12371 13823 0
        3 185 184 9064 0
        4 182 181 179 0
        5 9958 2688 9045 0
        6 199 7650 186 0
        7 11769 3828 11770 0
        8 16830 11819 184 0
        9 10984 7295 10831 0
        10 20584 20493 6193 0"""
    )


def pseudo_dotmesh_broken():
    return textwrap.dedent(
        """100079 1000 10 LONG/LAT
        1	        9.5552751717	       55.7048492992	   -1.10263693332672	1
        2	          9.55555483	       55.7070180551	   -1.07409691810608	1
        38031 weee 4 25
        1 178 179 181 0
        2 3912 12371 13823 0
        3 185 184 9064 0
        10 20584 20493 6193 0"""
    )


def pseudo_dotmesh_bad_crs():
    return textwrap.dedent(
        """100079 1000 10 NOTRIGHT
        1	        9.5552751717	       55.7048492992	   -1.10263693332672	1
        2	          9.55555483	       55.7070180551	   -1.07409691810608	1
        38031 weee 4 25
        1 178 179 181 0
        2 3912 12371 13823 0
        3 185 184 9064 0
        10 20584 20493 6193 0"""
    )


def garbage():
    return "hi"


def empty():
    return ""


@pytest.mark.parametrize(
    "datafun,status_code",
    [
        (pseudo_dotmesh_ok, 200),
        (pseudo_dotmesh_broken, 400),
        (pseudo_dotmesh_bad_crs, 400),
        (garbage, 400),
        (empty, 400),
    ],
)
def test_convert(flask_client, datafun, status_code):
    data = datafun()
    assert isinstance(data, str)
    rv = flask_client.post("/convert", data=data)

    assert rv.status_code == status_code
    if status_code == 200:
        assert rv.json
