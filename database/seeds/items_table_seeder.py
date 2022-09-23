from datetime import datetime

from app.models.pydantic.item import Item
from app.repositories.item_repository import ItemRepository


class ItemTableSeeder:
    async def execute(self):
        items = [
            Item(
                id=1,
                name="Cerveja",
                price=9,
                inventory_id="40000010019",
                aggregator_id="1042777",
                item_type="BEBIDAS",
                subtype="",
                ncm="2203.00.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=2,
                name="Cheeseburguer",
                price=14,
                inventory_id="40000010002",
                aggregator_id="946637",
                item_type="PRINCIPAL",
                subtype="",
                ncm="2106.90.90",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=3,
                name="Cheesebacon",
                price=18.5,
                inventory_id="40000010005",
                aggregator_id="946638",
                item_type="PRINCIPAL",
                subtype="",
                ncm="2106.90.90",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=4,
                name="Cheesesalada",
                price=17,
                inventory_id="40000010004",
                aggregator_id="946639",
                item_type="PRINCIPAL",
                subtype="",
                ncm="2106.90.90",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=5,
                name="Original",
                price=15.5,
                inventory_id="40000010003",
                aggregator_id="946640",
                item_type="PRINCIPAL",
                subtype="",
                ncm="2106.90.90",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=6,
                name="Batata Frita",
                price=9,
                inventory_id="40000010001",
                aggregator_id="946642",
                item_type="ACOMPANHAMENTO",
                subtype="",
                ncm="2106.90.90",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=7,
                name="Coca Cola",
                price=6,
                inventory_id="1022000002",
                aggregator_id="946644",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=8,
                name="Coca Cola sem Açúcar",
                price=6,
                inventory_id="10038000002",
                aggregator_id="948163",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=9,
                name="Sprite",
                price=6,
                inventory_id="10026000001",
                aggregator_id="946645",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=10,
                name="Fanta Laranja",
                price=6,
                inventory_id="10035000002",
                aggregator_id="948165",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=11,
                name="Guaraná",
                price=6,
                inventory_id="10025000002",
                aggregator_id="946656",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=12,
                name="Cheeseburguer + Batata Frita + Bebida",
                price=29,
                inventory_id="40000010006",
                aggregator_id="946653",
                item_type="COMBOS",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=13,
                name="Cheesebacon + Batata Frita + Bebida",
                price=33.5,
                inventory_id="40000010009",
                aggregator_id="946662",
                item_type="COMBOS",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=14,
                name="Cheesesalada + Batata Frita + Bebida",
                price=32,
                inventory_id="40000010008",
                aggregator_id="946663",
                item_type="COMBOS",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=15,
                name="Original + Batata Frita + Bebida",
                price=31.5,
                inventory_id="40000010007",
                aggregator_id="946664",
                item_type="COMBOS",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=16,
                name="Combo Heineken (2 LANCHES, 1 BATATA, 2 HEINEKEN)",
                price=55,
                inventory_id="40000010030",
                aggregator_id="1680490",
                item_type="COMBOS",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=17,
                name="Não, sem sachê",
                price=0,
                inventory_id="0",
                aggregator_id="950291",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=18,
                name="Sim, com sachê",
                price=0,
                inventory_id="10039",
                aggregator_id="950290",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=19,
                name="Combo Heineken (LANCHE + 1 BATATA + 1 HEINEKEN)",
                price=30,
                inventory_id="40000010010",
                aggregator_id="1042860",
                item_type="COMBOS",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=20,
                name="Retirar Picles",
                price=0,
                inventory_id="1681626",
                aggregator_id="1681626",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=21,
                name="Retirar Cebola",
                price=0,
                inventory_id="1681625",
                aggregator_id="1681625",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=22,
                name="Sachê de Maionese, Mostarda e Ketchup",
                price=0,
                inventory_id="1681629",
                aggregator_id="1681629",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=23,
                name="Trocar carne por batatoburger",
                price=0,
                inventory_id="1681628",
                aggregator_id="1681628",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=24,
                name="Retirar queijo",
                price=0,
                inventory_id="1678975",
                aggregator_id="1678975",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=25,
                name="Retirar Picles",
                price=0,
                inventory_id="1678977",
                aggregator_id="1678977",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=26,
                name="Retirar Cebola",
                price=0,
                inventory_id="1678978",
                aggregator_id="1678978",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=27,
                name="Retirar Mostarda e Ketchup",
                price=0,
                inventory_id="1681627",
                aggregator_id="1681627",
                item_type="COMPLEMENTO",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=28,
                name="agua com gas crystal T",
                price=8,
                inventory_id="948167",
                aggregator_id="948167",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=29,
                name="agua sem gas crystal T",
                price=8,
                inventory_id="948166",
                aggregator_id="948166",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=30,
                name="KIT Cine Drive In",
                price=114,
                inventory_id="663298",
                aggregator_id="663298",
                item_type="COMBOS",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=31,
                name="Torta De Nutella",
                price=18,
                inventory_id="1039108",
                aggregator_id="1039108",
                item_type="DOCES",
                subtype="",
                ncm="2007.99.23",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=32,
                name="Torta Banoffee",
                price=18,
                inventory_id="1039106",
                aggregator_id="1039106",
                item_type="DOCES",
                subtype="",
                ncm="2007.99.23",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=33,
                name="Chá Tamarindo 500 ml",
                price=6,
                inventory_id="1689692",
                aggregator_id="1689692",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=34,
                name="Chá Mate com Limão 500 ml",
                price=6,
                inventory_id="1689693",
                aggregator_id="1689693",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=35,
                name="Chá Tamarindo 1L",
                price=10,
                inventory_id="1689694",
                aggregator_id="1689694",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=36,
                name="Chá Mate com Limão 1L",
                price=10,
                inventory_id="1689696",
                aggregator_id="1689696",
                item_type="BEBIDAS",
                subtype="",
                ncm="2202.10.00",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=37,
                name="Vegetariano",
                price=12.5,
                inventory_id="856637",
                aggregator_id="856637",
                item_type="PRINCIPAL",
                subtype="",
                ncm="2106.90.90",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=38,
                name="Combo Vegetariano",
                price=27.5,
                inventory_id="449464",
                aggregator_id="449464",
                item_type="COMBOS",
                subtype="",
                ncm="Not Taxable",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
            Item(
                id=39,
                name="Bag Térmica Patties",
                price=33,
                inventory_id="1689233",
                aggregator_id="1689233",
                item_type="PRODUTOS ESPECIAIS",
                subtype="",
                ncm="42029900",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
        ]

        repository = ItemRepository()
        repository.save_many(items)
