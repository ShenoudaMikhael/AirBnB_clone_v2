"""Console Module Test cases"""
import unittest
import json
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestConsole(unittest.TestCase):
    """Test Console class"""
    def setUp(self):
        """setUp"""
        self.console = HBNBCommand()
        try:
            os.remove("file.json")
        except Exception:
            pass

    def tearDown(self):
        """
        Remove temporary file (file.json) created as a result
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_quit_command(self):
        """test_quit_command"""
        with self.assertRaises(SystemExit):

            self.assertTrue(self.console.onecmd("quit"))

    def test_eof_command(self):
        """test_eof_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue().strip(), "")

    def test_docstrings(self):
        """checking for docstrings"""
        self.assertIsNotNone(self.console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_wrong_command(self):
        """test_eof_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("wrongComand")
            self.assertEqual(
                f.getvalue().strip(), "name 'wrongComand' is not defined")

    def test_help_command(self):
        """test_help_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_custom_prompt(self):
        """test_custom_prompt"""
        self.assertEqual(self.console.prompt, "(hbnb) ")

    def test_empty_line(self):
        """test_empty_line"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd(""))
            self.assertEqual(f.getvalue().strip(), "")

    # create
    def test_create_command(self):
        """test_create_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """test_create_invalid_class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class(self):
        """test_create_valid_class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create BaseModel"))
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show_command(self):
        """test_show_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_missing_class(self):
        """test_show_missing_class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """test_show_missing_id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel"))
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_no_instance_found(self):
        """test_show_no_instance_found"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel 121212"))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_command(self):
        """test_destroy_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_missing_class(self):
        """test_destroy_missing_class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """test_destroy_missing_id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel"))
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_no_instance_found(self):
        """test_destroy_no_instance_found"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel 121212"))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all_command(self):
        """test_all_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all"))
            for item in json.loads(f.getvalue().strip()):
                models = [
                    "[User]",
                    "[BaseModel]",
                    "[City]",
                    "[Amenity]",
                    "[Place]",
                    "[Review]",
                    "[State]",
                ]
                self.assertIn(item.split()[0], models)

    def test_all_with_class_name(self):
        """test_all_with_class_name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all BaseModel"))

            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], "[BaseModel]")

    def test_all_with_invalid_class_name(self):
        """test_all_with_invalid_class_name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_command(self):
        """test_update_command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_missing_class(self):
        """test_update_missing_class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """test_update_missing_id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel"))
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_no_instance_found(self):
        """test_update_no_instance_found"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel 121212"))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attribute(self):
        """test_update_missing_attribute"""
        with patch("sys.stdout", new=StringIO()) as f:
            instance = BaseModel()
            self.assertFalse(
                self.console.onecmd(f"update BaseModel {instance.id}"))
            self.assertEqual(
                f.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_value(self):
        """test_update_missing_value"""
        with patch("sys.stdout", new=StringIO()) as f:
            instance = BaseModel()
            self.assertFalse(
                self.console.onecmd(f"update BaseModel {instance.id} email")
            )
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    # BaseModel value cases
    def test_command_create_BaseModel(self):
        """test_command_create_BaseModel"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIn(f"BaseModel.{output}", storage.all().keys())

    def test_command_create_User(self):
        """test_command_create_User"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertIn(f"User.{output}", storage.all().keys())

    def test_command_create_City(self):
        """test_command_create_City"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create City")
            output = f.getvalue().strip()
            self.assertIn(f"City.{output}", storage.all().keys())

    def test_command_create_Amenity(self):
        """test_command_create_Amenity"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            output = f.getvalue().strip()
            self.assertIn(f"Amenity.{output}", storage.all().keys())

    def test_command_create_Place(self):
        """test_command_create_Place"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Place")
            output = f.getvalue().strip()
            self.assertIn(f"Place.{output}", storage.all().keys())

    def test_command_create_Review(self):
        """test_command_create_Review"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Review")
            output = f.getvalue().strip()
            self.assertIn(f"Review.{output}", storage.all().keys())

    def test_command_create_State(self):
        """test_command_create_State"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create State")
            output = f.getvalue().strip()
            self.assertIn(f"State.{output}", storage.all().keys())

    def test_command_count_User(self):
        """test_command_count_User"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(
                output, str(len([
                    k for k in storage.all() if k.split(".")[0] == "User"]))
            )

    def test_command_update_User(self):
        """test_command_update_User"""
        with patch("sys.stdout", new=StringIO()) as f:
            instance = User()
            instance.email = "ABC"
            self.assertEqual("ABC", instance.email)
            self.console.onecmd(
                "update User {} email testemail".format(instance.id))
            self.assertEqual("testemail", instance.email)

    def test_command_update_User_dict(self):
        """test_command_update_User_dict"""
        with patch("sys.stdout", new=StringIO()) as f:
            instance = User()
            instance.last_name = "ABC"
            instance.first_name = "first_name"
            self.assertEqual("ABC", instance.last_name)
            qqq = "User.update('{}',{}{}".format(
                instance.id,
                "{'first_name':'new_name',",
                "'last_name':'new_last_name'})")
            self.console.onecmd(qqq)
            self.assertEqual("new_last_name", instance.last_name)
            self.assertEqual("new_name", instance.first_name)

    def test_command_update_User_args(self):
        """test_command_update_User_args"""
        with patch("sys.stdout", new=StringIO()) as f:
            instance = User()
            instance.first_name = "first_name"
            self.assertEqual("first_name", instance.first_name)
            qqq = "User.update('{}','{}','{}')".format(
                instance.id,
                "first_name",
                "new_name")
            self.console.onecmd(qqq)
            self.assertEqual("new_name", instance.first_name)

    def test_command_destroy_User_args(self):
        """test_command_destroy_User_args"""
        with patch("sys.stdout", new=StringIO()) as f:
            instance = User()
            self.assertIn("User.{}".format(instance.id), storage.all())
            qqq = "User.destroy('{}')".format(instance.id)
            self.console.onecmd(qqq)
            self.assertNotIn("User.{}".format(instance.id), storage.all())

    def test_command_show(self):
        """test_command_show"""
        with patch("sys.stdout", new=StringIO()) as f:
            instance = User()

            qqq = "User.show('{}')".format(instance.id)
            self.console.onecmd(qqq)
            result = f.getvalue().strip()
            self.assertEqual("{}".format(instance.__str__()), result)


if __name__ == "__main__":
    unittest.main()
