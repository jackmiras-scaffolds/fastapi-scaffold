#  import asyncio
#
#  import pytest
#  from configs.constants import Constants
#  from app.repositories.item_repository import ItemRepository
#  from configs.database import db
#
#
#  @pytest.fixture()
#  def random_aggregator_id():
#      item_repository = ItemRepository()
#      random_item = asyncio.run(item_repository.random_item())
#      yield random_item.aggregator_id
#
#
#  def test_get_item_success(test_client, random_aggregator_id):
#      uri = f"{Constants.API_V1}/items?aggregator_id={random_aggregator_id}"
#      db.commit()
#      response_from_api = test_client.get(uri)
#      assert response_from_api.status_code == Constants.HTTP_OK
#
#
#  def test_get_item_fail(test_client):
#      uri = f"{Constants.API_V1}/items?aggregator_id="
#      db.commit()
#      response_from_api = test_client.get(uri)
#      assert response_from_api.status_code == Constants.HTTP_NOT_FOUND
