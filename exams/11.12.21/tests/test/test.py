from project.team import Team
from unittest import TestCase

class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team('Team')

    def test_team_init(self):
        team_name = 'Test'
        team = Team(team_name)

        self.assertEqual(team_name, team.name)
        self.assertEqual({}, team.members)

    def test_name_setter_raises_when_name_contains_non_alpha_letters(self):
        with self.assertRaises(ValueError) as contex:
            team = Team('123asdASD.,$@!$%?!')
        self.assertEqual('Team Name can contain only letters!', str(contex.exception))

    def test_add_member_add_only_new_players_to_the_team(self):
        self.team.members['ivan'] = 18
        result = self.team.add_member(ivan=18, pesho=21, gosho=24)
        self.assertEqual(f"Successfully added: pesho, gosho", result)
        self.assertEqual(18, self.team.members['ivan'])
        self.assertEqual(21, self.team.members['pesho'])
        self.assertEqual(24, self.team.members['gosho'])

    def test_remove_member_returns_error_message_when_player_does_not_exist(self):
        member_name = 'Gosho'
        result = self.team.remove_member(member_name)
        self.assertEqual(f"Member with name {member_name} does not exist", result)

    def test_remove_member_remove_member_from_the_team(self):
        self.team.members['gosho'] = 21
        self.team.members['pesho'] = 19
        result = self.team.remove_member('gosho')

        self.assertEqual(f"Member gosho removed", result)
        self.assertEqual(19, self.team.members['pesho'])
        self.assertTrue('gosho' not in self.team.members)

    def test_gt_compare_teams_by_members_count(self):
        self.team.members['gosho'] = 22
        self.team.members['pesho'] = 21

        another_team = Team('anotherTeam')
        another_team.members['member1'] = 12
        another_team.members['member2'] = 15
        another_team.members['member3'] = 19

        self.assertEqual(True, another_team > self.team)
        self.assertEqual(False, another_team < self.team)

    def test_len_returns_correct_members_count(self):
        self.team.members['gosho'] = 21
        self.team.members['pesho'] = 25

        self.assertEqual(2, len(self.team))

    def test_add_returns_new_team_with_combined_members(self):
        self.team.members['gosho'] = 22
        self.team.members['pesho'] = 21

        another_team = Team('Another')
        another_team.members['member1'] = 12
        another_team.members['member2'] = 15
        another_team.members['member3'] = 19

        result = self.team + another_team
        expected_result_members = {
            'gosho': 22,
            'pesho': 21,
            'member1': 12,
            'member2': 15,
            'member3': 19
        }
        self.assertEqual('TeamAnother', result.name)
        self.assertEqual(expected_result_members, result.members)

    def test_str_returns_members_sorted_in_descending_orders_by_age_in_proper_string_format(self):
        self.team.members['member1'] = 12
        self.team.members['member2'] = 15
        self.team.members['member3'] = 19

        result = str(self.team)
        expected = f'Team name: Team\n' + \
                    f'Member: member3 - 19-years old\n' + \
                    f'Member: member2 - 15-years old\n' + \
                    f'Member: member1 - 12-years old'

        self.assertEqual(expected, result)
