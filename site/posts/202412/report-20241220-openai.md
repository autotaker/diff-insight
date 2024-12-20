---
date: '2024-12-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ebedb4...MicrosoftDocs:53fdfa0
summary: このコードの変更は、Azure GovernmentにおけるOpenAI機能に関する情報を強化するものであり、新しい「Azure OpenAIの特徴」セクションが追加されました。このセクションでは、特にAzure
  Government向けのOpenAI機能の制限とサポート状況が詳しく説明されています。また、全体として20箇所の変更があり、削除が9箇所、追加が11箇所含まれています。ブレイキングチェンジは明記されていないものの、特定の機能制限があり、ユーザーによっては影響があると考えられます。この更新により、政府機関がOpenAIを利用する際の技術的な制約や機能に関する理解が深まり、システム設計や運用の指針となる重要な情報が提供されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ebedb4...MicrosoftDocs:53fdfa0){target="_blank"}

# ハイライト
このコードの変更は、Azure GovernmentにおけるOpenAI機能についての情報を拡充するものです。具体的には新しいセクション「Azure OpenAIの特徴」が追加され、特にAzure Government向けに提供されるOpenAI機能の詳細が記されています。

## 新機能
- 「Azure OpenAIの特徴」セクションが新たに追加されました。
- Azure GovernmentにおけるOpenAIの機能制限やサポート状況の詳細が明示されました。

## ブレイキングチェンジ
- 特にブレイキングチェンジは記載されていないが、特定の機能の制限が追加されたため、ユーザーの解釈によってはブレイキングと見做される可能性があります。

## その他の更新
- 構造的には、削除9箇所と追加11箇所を含む、計20箇所の変更がなされています。

# 洞察
この更新で強調されるのは、Azure Government向けに特化したOpenAIの利用制限とサポート内容です。特に、Azure環境で政府機関がOpenAIを利用する場合に知っておくべき技術的な制約や機能の詳細が記されており、ユーザーがシステムを構築・運用する上での指針が示されています。

たとえば、Azure Governmentでは一般的なAzure応用例と異なり、構造化出力や予約購入、バッチ展開など多くの機能がサポートされていません。このことは、政府向けの特別なセキュリティやコンプライアンス要件が背景にあると推測されます。

また、データの接続先についても、仮想ネットワークやプライベートリンク経由が推奨される一方で、一般的なWebアプリへのデプロイ方法は提供されていない点も重要です。しかし、監視機能やデータストレージ、そしてコンプライアンスに関連する事項については詳細に触れられているため、今後の運用や法令対応の計画立案に役立つ情報が提供されています。

この情報の追加により、Azure GovernmentでのAIサービス活用に関する理解がより詳細になり、担当者がどのようにシステムを設計・搭載するのかを考える際の貴重なリソースとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-government.md](#item-a47549) | minor update | Azure Government向けのOpenAI機能に関する更新 | modified | 11 | 9 | 20 | 


# Modified Contents
## articles/ai-services/openai/azure-government.md{#item-a47549}

<details>
<summary>Diff</summary>
````diff
@@ -50,17 +50,19 @@ To request quota increases for these models, submit a request at [https://aka.ms
 
 ## Azure OpenAI features
 
+The following feature differences exist when comparing Azure OpenAI in Azure Government vs commercial cloud.
+
 |Feature|Description|
 |--------|--------|
-| Connect your data | Available in USGovVirginia and USGovArizona. Virtual network and private links are supported. Deployment to a web app or a copilot in Copilot Studio is not supported. |
-|Managed Identity|Yes, via Microsoft Entra ID|
-|Virtual network support & private link support| Yes. |
-|UI experience|**Azure portal** for account & resource management<br>**Azure OpenAI Studio** for model exploration|
-|Abuse Monitoring|Not all features of Abuse Monitoring are enabled for Azure OpenAI in Azure Government. You are responsible for implementing reasonable technical and operational measures to detect and mitigate any use of the service in violation of the Product Terms. [Automated Content Classification and Filtering](./concepts/content-filter.md) remains enabled by default for Azure Government. If modified content filters are required, apply at [https://aka.ms/AOAIGovModifyContentFilter](https://aka.ms/AOAIGovModifyContentFilter)|
-|Data Storage|In Azure Government, there are no Azure OpenAI features currently enabled that store customer data at rest. However, Customer Managed Keys (CMK) can still be enabled in Azure Government to support use of the same policies in Azure Government as in Public cloud. Note also that if Azure OpenAI features that store customer data are enabled in Azure Government in the future, any existing CMK deployment would be applied to that data at that time. Learn more at [Azure OpenAI Data Privacy](/../legal/cognitive-services/openai/data-privacy).|
-|Compliance|View the current status of Azure OpenAI compliance in Azure Government at [Azure Government Services Audit Scope](/azure/azure-government/compliance/azure-services-in-fedramp-auditscope?branch=pr-en-us-76518#azure-government-services-by-audit-scope)|
-|Service Endpoints|openai.azure.us|
-|Key Portals|<ul></li><li>Azure OpenAI Studio - aoai.azure.us</li><li>Azure portal - portal.azure.us</li></ul>|
+| Structured Outputs | Not currently supported. |
+| Reservation Based Purchases | Not currently supported. |
+| Batch Deployments | Not currently supported. |
+| Connect your data | Virtual network and private links are supported. Deployment to a web app or a copilot in Copilot Studio is not supported. |
+| Abuse Monitoring | Not all features of Abuse Monitoring are enabled for Azure OpenAI in Azure Government. You are responsible for implementing reasonable technical and operational measures to detect and mitigate any use of the service in violation of the Product Terms. [Automated Content Classification and Filtering](./concepts/content-filter.md) remains enabled by default for Azure Government. If modified content filters are required, apply at [https://aka.ms/AOAIGovModifyContentFilter](https://aka.ms/AOAIGovModifyContentFilter)|
+| Data Storage | In Azure Government, there are no Azure OpenAI features currently enabled that store customer data at rest. However, Customer Managed Keys (CMK) can still be enabled in Azure Government to support use of the same policies in Azure Government as in Public cloud. Note also that if Azure OpenAI features that store customer data are enabled in Azure Government in the future, any existing CMK deployment would be applied to that data at that time. Learn more at [Azure OpenAI Data Privacy](/../legal/cognitive-services/openai/data-privacy).|
+| Compliance | View the current status of Azure OpenAI compliance in Azure Government at [Azure Government Services Audit Scope](/azure/azure-government/compliance/azure-services-in-fedramp-auditscope?branch=pr-en-us-76518#azure-government-services-by-audit-scope)|
+| Service Endpoints | openai.azure.us |
+| Key Portals | <ul></li><li>Azure OpenAI Studio - aoai.azure.us</li><li>Azure portal - portal.azure.us</li></ul> |
 
 <br>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Government向けのOpenAI機能に関する更新"
}
```

### Explanation
このコードの変更では、Azure GovernmentにおけるOpenAI機能の違いについての情報が追加されました。変更内容は、全体で20の変更、11の追加および9の削除が含まれています。新たに「Azure OpenAIの特徴」セクションが追加され、Azure Governmentで利用可能なOpenAI機能に関する特記事項が詳細に記載されています。

新たに追加された特徴には、構造化出力や予約購入、バッチ展開がサポートされていないこと、データの接続については仮想ネットワークやプライベートリンクがサポートされているが、WebアプリやCopilot Studioへのデプロイはサポートされないことが示されています。また、監視機能やデータストレージ、コンプライアンスの状況も具体的に述べられ、利用者が遵守すべき事項や今後の期待などが明確に伝えられています。これにより、Azure GovernmentでのOpenAI利用に関する理解が深まり、使用に際して留意すべき事項を把握することができます。


