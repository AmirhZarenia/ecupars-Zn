from rest_framework import serializers
from .models import ChatSession, Message, Advertisement, Map, IssueCategory, Issue, Question, DiagnosticStep, Option, SubscriptionPlan, UserSubscription
from .models import Tag, Solution, Article

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['id', 'title', 'image', 'category']



class IssueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueCategory
        fields = '__all__'

    def get_root_category(self, obj):
        root_category = obj.get_root_category()
        return IssueCategorySerializer(root_category).data

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'





class DiagnosticStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticStep
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'



# سریالایزر پلن‌ها
class SubscriptionPlanSerializer(serializers.ModelSerializer):
    access_to_categories = IssueCategorySerializer(many=True, read_only=True)

    class Meta:
        model = SubscriptionPlan
        fields = "__all__"

# سریالایزر اشتراک کاربران
class UserSubscriptionSerializer(serializers.ModelSerializer):
    plan = SubscriptionPlanSerializer(read_only=True)
    active_categories = IssueCategorySerializer(many=True, read_only=True)

    class Meta:
        model = UserSubscription
        fields = ["plan", "active_categories", "start_date", "end_date", "is_active"]

    


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'link', 'banner', 'created_at']





class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = ['id','session', 'sender', 'content', 'timestamp', 'sender_name']

class ChatSessionSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = ['id', 'user', 'consultant', 'is_active', 'created_at', 'messages']





class SearchResultSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
    data = serializers.SerializerMethodField()

    def get_data(self, obj):
        if obj['type'] == 'car':
            car = obj['data']['car']
            return {"car": IssueCategorySerializer(car).data}
        elif obj['type'] == 'issue':
            issue = obj['data']['issue']
            return {
                "issue": IssueSerializer(issue).data,
                "full_category_name": obj['data']['full_category_name']
            }
        elif obj['type'] == 'solution':
            solution = obj['data']['solution']
            return {
                "solution": SolutionSerializer(solution).data,
                "issue": IssueSerializer(obj['data']['issue']).data,
                "full_category_name": obj['data']['full_category_name']
            }
        elif obj['type'] == 'tag':
            if 'issue' in obj['data']:
                return {
                    "tag": TagSerializer(obj['data']['tag']).data,
                    "issue": IssueSerializer(obj['data']['issue']).data,
                    "full_category_name": obj['data']['full_category_name']
                }
            elif 'solution' in obj['data']:
                return {
                    "tag": TagSerializer(obj['data']['tag']).data,
                    "solution": SolutionSerializer(obj['data']['solution']).data,
                    "issue": IssueSerializer(obj['data']['issue']).data,
                    "full_category_name": obj['data']['full_category_name']
                }
        return {}





class SolutionSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True)
    class Meta:
        model = Solution
        fields = ['id', 'title', 'description', 'issues']



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    question = QuestionSerializer(read_only=True)
    category = IssueCategorySerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'question']