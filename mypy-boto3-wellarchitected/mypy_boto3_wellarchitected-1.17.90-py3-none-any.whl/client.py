"""
Type annotations for wellarchitected service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_wellarchitected import WellArchitectedClient

    client: WellArchitectedClient = boto3.client("wellarchitected")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import (
    PermissionTypeType,
    ShareInvitationActionType,
    WorkloadEnvironmentType,
    WorkloadImprovementStatusType,
)
from .type_defs import (
    CreateMilestoneOutputTypeDef,
    CreateWorkloadOutputTypeDef,
    CreateWorkloadShareOutputTypeDef,
    GetAnswerOutputTypeDef,
    GetLensReviewOutputTypeDef,
    GetLensReviewReportOutputTypeDef,
    GetLensVersionDifferenceOutputTypeDef,
    GetMilestoneOutputTypeDef,
    GetWorkloadOutputTypeDef,
    ListAnswersOutputTypeDef,
    ListLensesOutputTypeDef,
    ListLensReviewImprovementsOutputTypeDef,
    ListLensReviewsOutputTypeDef,
    ListMilestonesOutputTypeDef,
    ListNotificationsOutputTypeDef,
    ListShareInvitationsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWorkloadSharesOutputTypeDef,
    ListWorkloadsOutputTypeDef,
    UpdateAnswerOutputTypeDef,
    UpdateLensReviewOutputTypeDef,
    UpdateShareInvitationOutputTypeDef,
    UpdateWorkloadOutputTypeDef,
    UpdateWorkloadShareOutputTypeDef,
)

__all__ = ("WellArchitectedClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class WellArchitectedClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_lenses(self, *, WorkloadId: str, LensAliases: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.associate_lenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#associate_lenses)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#can_paginate)
        """

    def create_milestone(
        self, *, WorkloadId: str, MilestoneName: str, ClientRequestToken: str
    ) -> CreateMilestoneOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.create_milestone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_milestone)
        """

    def create_workload(
        self,
        *,
        WorkloadName: str,
        Description: str,
        Environment: WorkloadEnvironmentType,
        ReviewOwner: str,
        Lenses: List[str],
        ClientRequestToken: str,
        AccountIds: List[str] = None,
        AwsRegions: List[str] = None,
        NonAwsRegions: List[str] = None,
        PillarPriorities: List[str] = None,
        ArchitecturalDesign: str = None,
        IndustryType: str = None,
        Industry: str = None,
        Notes: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateWorkloadOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.create_workload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_workload)
        """

    def create_workload_share(
        self,
        *,
        WorkloadId: str,
        SharedWith: str,
        PermissionType: PermissionTypeType,
        ClientRequestToken: str
    ) -> CreateWorkloadShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.create_workload_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_workload_share)
        """

    def delete_workload(self, *, WorkloadId: str, ClientRequestToken: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.delete_workload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_workload)
        """

    def delete_workload_share(
        self, *, ShareId: str, WorkloadId: str, ClientRequestToken: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.delete_workload_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_workload_share)
        """

    def disassociate_lenses(self, *, WorkloadId: str, LensAliases: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.disassociate_lenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#disassociate_lenses)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#generate_presigned_url)
        """

    def get_answer(
        self, *, WorkloadId: str, LensAlias: str, QuestionId: str, MilestoneNumber: int = None
    ) -> GetAnswerOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.get_answer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_answer)
        """

    def get_lens_review(
        self, *, WorkloadId: str, LensAlias: str, MilestoneNumber: int = None
    ) -> GetLensReviewOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_lens_review)
        """

    def get_lens_review_report(
        self, *, WorkloadId: str, LensAlias: str, MilestoneNumber: int = None
    ) -> GetLensReviewReportOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_review_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_lens_review_report)
        """

    def get_lens_version_difference(
        self, *, LensAlias: str, BaseLensVersion: str
    ) -> GetLensVersionDifferenceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_version_difference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_lens_version_difference)
        """

    def get_milestone(self, *, WorkloadId: str, MilestoneNumber: int) -> GetMilestoneOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.get_milestone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_milestone)
        """

    def get_workload(self, *, WorkloadId: str) -> GetWorkloadOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.get_workload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_workload)
        """

    def list_answers(
        self,
        *,
        WorkloadId: str,
        LensAlias: str,
        PillarId: str = None,
        MilestoneNumber: int = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListAnswersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_answers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_answers)
        """

    def list_lens_review_improvements(
        self,
        *,
        WorkloadId: str,
        LensAlias: str,
        PillarId: str = None,
        MilestoneNumber: int = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLensReviewImprovementsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_lens_review_improvements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_lens_review_improvements)
        """

    def list_lens_reviews(
        self,
        *,
        WorkloadId: str,
        MilestoneNumber: int = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLensReviewsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_lens_reviews)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_lens_reviews)
        """

    def list_lenses(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListLensesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_lenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_lenses)
        """

    def list_milestones(
        self, *, WorkloadId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMilestonesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_milestones)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_milestones)
        """

    def list_notifications(
        self, *, WorkloadId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListNotificationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_notifications)
        """

    def list_share_invitations(
        self, *, WorkloadNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListShareInvitationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_share_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_share_invitations)
        """

    def list_tags_for_resource(self, *, WorkloadArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_tags_for_resource)
        """

    def list_workload_shares(
        self,
        *,
        WorkloadId: str,
        SharedWithPrefix: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListWorkloadSharesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_workload_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_workload_shares)
        """

    def list_workloads(
        self, *, WorkloadNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkloadsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.list_workloads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_workloads)
        """

    def tag_resource(self, *, WorkloadArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#tag_resource)
        """

    def untag_resource(self, *, WorkloadArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#untag_resource)
        """

    def update_answer(
        self,
        *,
        WorkloadId: str,
        LensAlias: str,
        QuestionId: str,
        SelectedChoices: List[str] = None,
        Notes: str = None,
        IsApplicable: bool = None
    ) -> UpdateAnswerOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.update_answer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_answer)
        """

    def update_lens_review(
        self,
        *,
        WorkloadId: str,
        LensAlias: str,
        LensNotes: str = None,
        PillarNotes: Dict[str, str] = None
    ) -> UpdateLensReviewOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.update_lens_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_lens_review)
        """

    def update_share_invitation(
        self, *, ShareInvitationId: str, ShareInvitationAction: ShareInvitationActionType
    ) -> UpdateShareInvitationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.update_share_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_share_invitation)
        """

    def update_workload(
        self,
        *,
        WorkloadId: str,
        WorkloadName: str = None,
        Description: str = None,
        Environment: WorkloadEnvironmentType = None,
        AccountIds: List[str] = None,
        AwsRegions: List[str] = None,
        NonAwsRegions: List[str] = None,
        PillarPriorities: List[str] = None,
        ArchitecturalDesign: str = None,
        ReviewOwner: str = None,
        IsReviewOwnerUpdateAcknowledged: bool = None,
        IndustryType: str = None,
        Industry: str = None,
        Notes: str = None,
        ImprovementStatus: WorkloadImprovementStatusType = None
    ) -> UpdateWorkloadOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.update_workload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_workload)
        """

    def update_workload_share(
        self, *, ShareId: str, WorkloadId: str, PermissionType: PermissionTypeType
    ) -> UpdateWorkloadShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.update_workload_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_workload_share)
        """

    def upgrade_lens_review(
        self, *, WorkloadId: str, LensAlias: str, MilestoneName: str, ClientRequestToken: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.90/reference/services/wellarchitected.html#WellArchitected.Client.upgrade_lens_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#upgrade_lens_review)
        """
