import httpx
from mcp.server.fastmcp import FastMCP

API_BASE = "http://127.0.0.1:8000"

mcp = FastMCP("船原滉樹API")

@mcp.tool()
def get_koju_info(
    school_name: str | None = None
):
    """
    船原滉樹の学歴情報を取得する。
    学校名を指定すると、その学校の情報のみを取得することができる。
    """

    if school_name is None:
        response = httpx.get(f"{API_BASE}/get_history")
        return response.text
    response = httpx.get(f"{API_BASE}/get_history/{school_name}")
    return response.text

if __name__ == "__main__":
    mcp.run(transport="stdio")