---
date: '2025-02-12'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f57bd77...MicrosoftDocs:be5df78
summary: このコード差分では、Azure OpenAIサービスの虚偽監視とコンテンツフィルタリングに関するドキュメントが軽微に更新され、情報提供がより明確になりました。新たに追加された注意書きでは、プロンプトやレスポンスが保存されず、フィルタリングシステムのトレーニングにユーザーの同意なしにそのデータが使用されないことが強調されています。互換性を破壊する変更はなく、虚偽監視における警告文の改善も行われました。この更新により、透明性と信頼性が向上し、特にプライバシー意識の高いユーザーにとって安心してサービスを利用できる環境が整いました。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f57bd77...MicrosoftDocs:be5df78){target="_blank"}

# ハイライト

このコード差分では、Azure OpenAIサービスの虚偽監視とコンテンツフィルタリングのドキュメントに軽微な更新が加えられました。新しい注意書きと文言の調整によって、ユーザーへの情報提供がより明確になっています。

## 新機能

- コンテンツフィルタリングにおいて、プロンプトやレスポンスが保存されないこと、フィルタリングシステムのトレーニングや改善にユーザーの同意なしに使用されないことに関する注意書きが追加されました。

## 互換性の破壊

- 今回の更新では互換性を破壊する変更はありません。

## その他の更新

- 虚偽監視における警告文の文言とリンク先の表現の調整により、情報の流れが改善されました。

# 知見

この更新は、Azure OpenAIが提供するサービスにおけるユーザーの透明性と信頼性を向上させる重要なステップです。虚偽監視においては、適切なレビューが行われない場合のリスクについて具体的な言及がなされることで、ユーザーはより慎重にサービスの利用を考慮することができます。これは特に、高度なAIシステムで誤ったフラグが立てられる可能性がある状況を認識するために重要です。

一方で、コンテンツフィルタリングに関する更新では、データプライバシーとセキュリティについて重要な情報が明確化されました。特に、この情報はプライバシー意識の高いユーザーに向けたもので、個人データがどのように扱われ、何がシステムに影響するのかを明示しています。これにより、ユーザーは安心してサービスを利用することができるでしょう。このような文言修正と注意書きの追加は、小さな変更に見えて、ユーザーエクスペリエンスと信頼性の向上に繋がる大きな一歩といえます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [abuse-monitoring.md](#item-b7afcb) | minor update | 軽微な更新: 虚偽監視に関する文書の修正 | modified | 2 | 2 | 4 | 
| [content-filter.md](#item-dfc7e7) | minor update | 軽微な更新: コンテンツフィルタリングに関する注意書きの追加 | modified | 3 | 0 | 3 | 


# Modified Contents
## articles/ai-services/openai/concepts/abuse-monitoring.md{#item-b7afcb}

<details>
<summary>Diff</summary>
````diff
@@ -32,10 +32,10 @@ There are several components to abuse monitoring:
 Some customers may want to use the Azure OpenAI Service for a use case that involves the processing of highly sensitive or highly confidential data, or otherwise may conclude that they do not want or do not have the right to permit Microsoft to store and conduct human review on their prompts and completions for abuse detection. To address these concerns, Microsoft allows customers who meet additional Limited Access eligibility criteria to apply to modify abuse monitoring by completing [this ](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOE9MUTFMUlpBNk5IQlZWWkcyUEpWWEhGOCQlQCN0PWcu)form. Learn more about applying for modified abuse monitoring at [Limited access to Azure OpenAI Service](/legal/cognitive-services/openai/limited-access?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext), and about the impact of modified abuse monitoring on data processing at [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=azure-portal).    
 
 > [!NOTE]
-> When abuse monitoring is modified and human review is not performed, detection of potential abuse may be less accurate. Customers will be notified of potential abuse detection as described above, and should be prepared to respond to such notification to avoid service interruption if possible.  
+> When abuse monitoring is modified and human review is not performed, detection of potential abuse may be less accurate. Customers are notified of potential abuse detection as described above, and should be prepared to respond to such notification to avoid service interruption if possible.  
 
 ## Next steps
 
 - Learn more about the [underlying models that power Azure OpenAI](../concepts/models.md).
 - Learn more about understanding and mitigating risks associated with your application: [Overview of Responsible AI practices for Azure OpenAI models](/legal/cognitive-services/openai/overview?context=/azure/ai-services/openai/context/context).
-- Learn more about how data is processed in connection with content filtering and abuse monitoring: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context#preventing-abuse-and-harmful-content-generation).
+- Learn more about how data is processed in content filtering and abuse monitoring: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context#preventing-abuse-and-harmful-content-generation).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "軽微な更新: 虚偽監視に関する文書の修正"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスの虚偽監視に関するドキュメントの軽微な更新を示しています。具体的には、2つの行が追加され、2つの行が削除され、全体として4つの変更が行われました。この変更は、虚偽監視が修正され人間のレビューが行われない場合、潜在的な虚偽の検出がより正確ではない可能性があることに関する警告文の文言の調整を含んでいます。さらに、文脈内のリンク先の表現も修正され、情報の流れが改善されています。この修正により、利用者に対する注意喚起がより明確になりました。

## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -24,6 +24,9 @@ In addition to the content filtering system, Azure OpenAI Service performs monit
 
 The following sections provide information about the content filtering categories, the filtering severity levels and their configurability, and API scenarios to be considered in application design and implementation. 
 
+> [!NOTE]
+> No prompts or completions are stored for the purposes of content filtering. No prompts or completions are used to train, retrain, or improve the content filtering system without your consent. For more information, see [Data, privacy, and security](/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=azure-portal).
+
 ## Content filter types
 
 The content filtering system integrated in the Azure OpenAI Service contains: 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "軽微な更新: コンテンツフィルタリングに関する注意書きの追加"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるコンテンツフィルタリングに関する文書に軽微な更新が加えられたことを示しています。具体的には、3つの行が追加され、削除はありません。更新された内容では、コンテンツフィルタリングの目的でプロンプトやレスポンスが保存されず、また、同意なしにはフィルタリングシステムのトレーニングや改善に使用されないことについての注意書きが追加されています。この情報は、データのプライバシーやセキュリティに関する詳細を参照する指示を含んでおり、ユーザーに対する透明性を高めています。これにより、ユーザーはコンテンツフィルタリングの運用に関して、より明確な理解を得ることができます。


