from rest_framework import serializers

Class ProductSerializer(serializers.Serializer):
    p_name = models.CharField(max_length=200)
    p_price = models.IntegerField()
    p_registerdate = models.DateTimeField(auto_now_add=True)
    p_company_name = models.ForeignKey(Company, on_delete=models.CASCADE)