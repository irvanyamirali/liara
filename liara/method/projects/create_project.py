from typing import Optional

import liara


class CreateProject:

    def create_project(
            self: "liara.Client",
            name: str,
            plan_id: str,
            platform: Optional[str] = None,
            network: Optional[str] = None
    ):
        """
        Create app that user owns
        :param plan_id: "enterprise", "standard", "free"
        """
        params: dict = {
            "name": name,
            "planID": plan_id,
            "platform": platform,
            "network": network
        }
        return self.api.execute(service="projects", method="post", data=params)