from aiohttp.test_utils import unittest_run_loop

from . import MockRoutesTestCase


# Create your tests here.
class ResourceTestCase(MockRoutesTestCase):
    @unittest_run_loop
    async def test_resource_delete(self):
        with self.mock_response() as rsps:
            rsps.add('GET', '/users/1', data={
                'id': 1,
                'username': 'user1',
                'group': 'watchers',
            })

            user1 = await self.generic_client.users.get(id=1)
            self.assertEqual(user1.username, 'user1')

        with self.mock_response() as rsps:
            rsps.add('DELETE', '/users/1', status=204)

            await user1.delete()

    @unittest_run_loop
    async def test_resource_delete_uuid(self):
        with self.mock_response() as rsps:
            rsps.add('GET', '/users/1', data={
                'uuid': 1,
                'username': 'user1',
                'group': 'watchers',
            })

            user1 = await self.generic_client.users.get(uuid=1)
            self.assertEqual(user1.username, 'user1')

        with self.mock_response() as rsps:
            rsps.add('DELETE', '/users/1', status=204)

            await user1.delete()

    @unittest_run_loop
    async def test_resource_save(self):
        with self.mock_response() as rsps:
            rsps.add('GET', '/users/1', data={
                'id': 1,
                'username': 'user1',
                'group': 'watchers',
            })

            user1 = await self.generic_client.users.get(id=1)
            self.assertEqual(user1.username, 'user1')

        with self.mock_response() as rsps:
            rsps.add('PUT', '/users/1', data={
                'id': 1,
                'username': 'user1',
                'group': 'admins',
            })

            user1.group = 'admins'
            await user1.save()

    @unittest_run_loop
    async def test_resource_save_uuid(self):
        with self.mock_response() as rsps:
            rsps.add('GET', '/users/1', data={
                'uuid': 1,
                'username': 'user1',
                'group': 'watchers',
            })

            user1 = await self.generic_client.users.get(uuid=1)
            self.assertEqual(user1.username, 'user1')

        with self.mock_response() as rsps:
            rsps.add('PUT', '/users/1', data={
                'uuid': 1,
                'username': 'user1',
                'group': 'admins',
            })

            user1.group = 'admins'
            await user1.save()